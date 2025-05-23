# core/chat_handler.py
from flask import jsonify
from utils.logger import info, error, debug, warning
from backend.utils.search_utils import perform_search # Added import
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
    current_scenario = data.get('current_scenario') # Extract current_scenario

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

    # Conditionally add contextual system message for Ollama
    if current_scenario:
        contextual_system_message = {
            "role": "system",
            "content": f"The student is currently focused on a '{current_scenario}' scenario. Please tailor your conversation, examples, and any exercises specifically to this context. Encourage role-playing within this scenario if appropriate. Maintain the established persona of Hey Gringo!."
        }
        # Insert after the main system prompt, which is the first message
        messages_for_ollama.insert(1, contextual_system_message)

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

        # Detect search command
        if ai_response.startswith("[SEARCH:") and ai_response.endswith("]"):
            search_query = ai_response[len("[SEARCH:"):-1].strip()
            
            if not search_query:
                info(f"AI requested a search but provided an empty query.", student_id=student_id)
                ai_response = "I considered searching for more information, but I didn't have a specific topic in mind. Could you please clarify what you'd like me to look up?"
            else:
                info(f"AI requested search for: {search_query}", student_id=student_id)
                search_results = perform_search(search_query)

                if search_results:
                    search_context_str = "Search Results:\n"
                for i, res in enumerate(search_results):
                    search_context_str += f"{i+1}. Title: {res['title']}\n   Snippet: {res['snippet']}\n   URL: {res['url']}\n"
                
                max_search_context_length = 2000 # Example character limit
                if len(search_context_str) > max_search_context_length:
                    search_context_str = search_context_str[:max_search_context_length] + "... (results truncated)"
                
                messages_for_reprompt = [
                    {"role": "system", "content": enhanced_prompt}, 
                    {
                        "role": "system",
                        "content": f"Based on the following information I found about '{search_query}':\n{search_context_str}\n\nNow, please provide a comprehensive and helpful answer to the user's original question: '{user_message}'. Remember to maintain your Hey Gringo! persona and answer naturally."
                    }
                    # Original user_message is included in the instruction above.
                ]
                
                info(f"Re-prompting Ollama with search results for query: {search_query}", student_id=student_id)
                try:
                    response_with_search = ollama.chat(
                        model=OLLAMA_CONFIG['MODEL'],
                        messages=messages_for_reprompt
                    )
                    ai_response = response_with_search['message']['content'] # This is the new AI response
                    info("Received search-informed response from Ollama.", student_id=student_id)
                except Exception as e_reprompt:
                    error(f"Error during Ollama re-prompt with search results: {e_reprompt}", student_id=student_id, traceback=traceback.format_exc())
                    ai_response = "I found some information, but I'm having a little trouble processing it right now. Could you try asking in a different way, or about something else?"
            else: # Search failed or no results
                info(f"Search for '{search_query}' yielded no results or failed.", student_id=student_id)
                ai_response = f"I tried looking that up ('{search_query}'), but I couldn't find specific information right now. Is there anything else I can help with?"

        # Now, ai_response is either the original, or search-informed, or a fallback.
        # Proceed with the rest of the logic:
        session.add_interaction("ai_response", ai_response)
        
        # Extrair e registrar tópicos cobertos (implementação básica)
        if "[Explicação]" in ai_response: # Check in the final ai_response
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