# core/chat_handler.py
from flask import jsonify
from utils.logger import info, error, debug, warning
import ollama
import time
import uuid
from core.session_manager import SessionManager
from core.config import SYSTEM_PROMPT, OLLAMA_CONFIG
import traceback

def calculate_points(user_message: str, ai_response: str, current_level: str) -> int:
    """Calcula pontos baseado na interação e nível do usuário."""
    # Pontos base pela participação
    base_points = min(len(user_message) // 10, 20)
    
    # Bônus por complexidade da resposta
    complexity_bonus = min(len(ai_response) // 50, 10)
    
    # Multiplicador baseado no nível
    level_multipliers = {
        'A1': 1.0, 'A2': 1.2, 'B1': 1.4,
        'B2': 1.6, 'C1': 1.8, 'C2': 2.0
    }
    level_multiplier = level_multipliers.get(current_level, 1.0)
    
    total_points = int((base_points + complexity_bonus) * level_multiplier)
    return total_points

def get_achievements(session) -> list:
    """Retorna lista de conquistas do usuário baseado em seu progresso."""
    achievements = []
    
    # Conquistas por número de tópicos
    topics_count = len(session.topics_covered)
    if topics_count >= 5:
        achievements.append({
            'id': 'topics_5',
            'title': 'Explorador Iniciante',
            'description': 'Completou 5 tópicos diferentes'
        })
    if topics_count >= 10:
        achievements.append({
            'id': 'topics_10',
            'title': 'Explorador Intermediário',
            'description': 'Completou 10 tópicos diferentes'
        })
    
    # Conquistas por nível alcançado
    level_achievements = {
        'B1': {'id': 'reach_b1', 'title': 'Comunicador Independente',
               'description': 'Alcançou o nível B1'},
        'C1': {'id': 'reach_c1', 'title': 'Mestre da Comunicação',
               'description': 'Alcançou o nível C1'}
    }
    if session.current_level in level_achievements:
        achievements.append(level_achievements[session.current_level])
    
    return achievements

def handle_chat_request(data):
    user_message = data.get('message')
    history = data.get('history', [])  # Histórico da conversa
    student_id = data.get('student_id') or str(uuid.uuid4())

    if not user_message:
        warning("Requisição sem mensagem", student_id=student_id)
        return jsonify({"error": "No message provided"}), 400

    # Gerenciar sessão do estudante
    session = SessionManager.get_session(student_id)
    session.add_interaction("user_message", user_message)
    
    debug("Processando mensagem do usuário", 
          student_id=student_id, 
          message_length=len(user_message),
          current_level=session.current_level,
          topics_count=len(session.topics_covered))

    # Adicionar informações de nível e progresso ao prompt do sistema
    enhanced_prompt = SYSTEM_PROMPT + f"""
    Current student level: {session.current_level}
    Topics covered: {', '.join(session.topics_covered)}
    Focus on progressive improvement and natural conversation.
    """

    messages_for_ollama = [{"role": "system", "content": enhanced_prompt}]
    for msg in history:
        messages_for_ollama.append({"role": msg['sender'], "content": msg['text']})
    messages_for_ollama.append({"role": "user", "content": user_message})

    try:
        info("Enviando requisição para Ollama", 
             student_id=student_id, 
             model=OLLAMA_CONFIG['MODEL'], 
             history_length=len(history))
        
        start_time = time.time()
        response = ollama.chat(
            model=OLLAMA_CONFIG['MODEL'],
            messages=messages_for_ollama
        )
        response_time = time.time() - start_time
        
        ai_response = response['message']['content']
        
        info("Resposta recebida do Ollama", 
             student_id=student_id,
             response_time_seconds=response_time,
             response_length=len(ai_response))
        
        # Atualizar a sessão com a resposta do AI
        session.add_interaction("ai_response", ai_response)
        
        # Extrair e registrar tópicos cobertos (implementação básica)
        if "[Explicação]" in ai_response:
            topic = ai_response.split("[Explicação]")[1].split("\n")[0].strip()
            session.add_topic(topic)
            info("Novo tópico registrado", student_id=student_id, topic=topic)

        # Sistema de gamificação aprimorado
        points_earned = calculate_points(user_message, ai_response, session.current_level)
        
        # Verificar progresso e atualizar nível se necessário
        session.update_level_based_on_progress()
        
        # Preparar feedback personalizado
        feedback = {
            "reply": ai_response,
            "student_id": student_id,
            "session_summary": session.get_session_summary(),
            "points_earned": points_earned,
            "level_progress": {
                "current_level": session.current_level,
                "topics_mastered": len(session.topics_covered),
                "next_level_topics": 5 - (len(session.topics_covered) % 5),  # Tópicos restantes para próximo nível
                "total_points": points_earned
            },
            "achievements": get_achievements(session)
        }
        
        return jsonify(feedback)
    except Exception as e:
        error("Erro ao processar chat com Ollama", 
              student_id=student_id,
              exception=str(e),
              traceback=traceback.format_exc())
        return jsonify({"error": str(e)}), 500