from typing import Dict, List, Optional
from datetime import datetime
import json
import os

class StudentSession:
    def __init__(self, student_id: str):
        self.student_id = student_id
        self.current_level = "A1"  # Nível inicial CEFR
        self.topics_covered: List[str] = []
        self.pronunciation_scores: Dict[str, float] = {}
        self.last_activity = datetime.now()
        self.session_history: List[Dict] = []
        self.current_conversation_id: Optional[str] = None
        self.load_session()

    def update_level(self, new_level: str) -> None:
        """Atualiza o nível do aluno baseado no desempenho."""
        self.current_level = new_level
        self.save_session()
        
    def update_level_based_on_progress(self) -> None:
        """Atualiza o nível do aluno baseado no número de tópicos cobertos.
        
        Esta função avalia o progresso do aluno com base no número de tópicos
        que ele cobriu durante as sessões de aprendizado e atualiza seu nível
        de proficiência de acordo com critérios predefinidos.
        
        Níveis CEFR: A1, A2, B1, B2, C1, C2
        """
        # Implementação da lógica de progressão de nível
        # Baseado no número de tópicos cobertos
        num_topics = len(self.topics_covered)
        
        # Definição dos limiares para progressão de nível
        if self.current_level == "A1" and num_topics >= 5:
            self.update_level("A2")
        elif self.current_level == "A2" and num_topics >= 10:
            self.update_level("B1")
        elif self.current_level == "B1" and num_topics >= 15:
            self.update_level("B2")
        elif self.current_level == "B2" and num_topics >= 20:
            self.update_level("C1")
        elif self.current_level == "C1" and num_topics >= 25:
            self.update_level("C2")

    def add_topic(self, topic: str) -> None:
        """Registra um novo tópico coberto na sessão."""
        if topic not in self.topics_covered:
            self.topics_covered.append(topic)
            self.save_session()

    def update_pronunciation_score(self, word: str, score: float) -> None:
        """Atualiza a pontuação de pronúncia para uma palavra específica."""
        self.pronunciation_scores[word] = score
        self.save_session()

    def add_interaction(self, interaction_type: str, content: str, conversation_id: Optional[str] = None) -> None:
        """Registra uma nova interação na sessão com ID de conversa opcional."""
        if conversation_id:
            self.current_conversation_id = conversation_id
        elif not self.current_conversation_id:
            self.current_conversation_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.session_history.append({
            "timestamp": datetime.now().isoformat(),
            "type": interaction_type,
            "content": content,
            "conversation_id": self.current_conversation_id
        })
        self.last_activity = datetime.now()
        self.save_session()

    def get_session_summary(self) -> Dict:
        """Retorna um resumo da sessão atual."""
        return {
            "student_id": self.student_id,
            "current_level": self.current_level,
            "topics_covered": self.topics_covered,
            "pronunciation_progress": self.pronunciation_scores,
            "last_activity": self.last_activity.isoformat(),
            "total_interactions": len(self.session_history),
            "current_conversation_id": self.current_conversation_id
        }

    def get_conversation_history(self, conversation_id: Optional[str] = None) -> List[Dict]:
        """Retorna o histórico de uma conversa específica ou da conversa atual."""
        target_id = conversation_id or self.current_conversation_id
        if not target_id:
            return []
        return [interaction for interaction in self.session_history 
                if interaction.get("conversation_id") == target_id]

    def get_last_conversation_summary(self) -> Dict:
        """Retorna um resumo da última conversa para retomada da aula."""
        if not self.session_history:
            return {"message": "Nenhuma aula anterior encontrada"}

        last_conversation = self.get_conversation_history()
        if not last_conversation:
            return {"message": "Nenhuma aula anterior encontrada"}

        topics_in_conversation = set()
        for interaction in last_conversation:
            if interaction["type"] == "topic":
                topics_in_conversation.add(interaction["content"])

        return {
            "last_activity": self.last_activity.isoformat(),
            "conversation_id": self.current_conversation_id,
            "topics_covered": list(topics_in_conversation),
            "current_level": self.current_level,
            "total_interactions": len(last_conversation),
            "last_interaction": last_conversation[-1] if last_conversation else None
        }

    def save_session(self) -> None:
        """Salva o estado atual da sessão em um arquivo JSON."""
        session_data = {
            "student_id": self.student_id,
            "current_level": self.current_level,
            "topics_covered": self.topics_covered,
            "pronunciation_scores": self.pronunciation_scores,
            "last_activity": self.last_activity.isoformat(),
            "session_history": self.session_history
        }
        
        os.makedirs("sessions", exist_ok=True)
        with open(f"sessions/{self.student_id}.json", "w") as f:
            json.dump(session_data, f, indent=2)

    def load_session(self) -> None:
        """Carrega uma sessão existente do arquivo JSON."""
        try:
            with open(f"sessions/{self.student_id}.json", "r") as f:
                data = json.load(f)
                self.current_level = data.get("current_level", self.current_level)
                self.topics_covered = data.get("topics_covered", [])
                self.pronunciation_scores = data.get("pronunciation_scores", {})
                self.last_activity = datetime.fromisoformat(data.get("last_activity", self.last_activity.isoformat()))
                self.session_history = data.get("session_history", [])
        except FileNotFoundError:
            # Sessão nova, usar valores padrão
            pass

class SessionManager:
    _instances: Dict[str, StudentSession] = {}

    @classmethod
    def get_session(cls, student_id: str) -> StudentSession:
        """Retorna uma sessão existente ou cria uma nova."""
        if student_id not in cls._instances:
            cls._instances[student_id] = StudentSession(student_id)
        return cls._instances[student_id]

    @classmethod
    def get_all_sessions(cls) -> List[Dict]:
        """Retorna um resumo de todas as sessões ativas."""
        return [session.get_session_summary() for session in cls._instances.values()]