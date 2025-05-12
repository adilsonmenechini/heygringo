# backend/test_session_manager.py
import unittest
from unittest.mock import patch, MagicMock
from session_manager import SessionManager, StudentSession
import uuid

class TestSessionManager(unittest.TestCase):
    def setUp(self):
        # Limpar o dicionário de sessões antes de cada teste
        SessionManager._sessions = {}
        
    def test_get_session_new_student(self):
        # Testar criação de nova sessão
        student_id = str(uuid.uuid4())
        session = SessionManager.get_session(student_id)
        
        # Verificar se a sessão foi criada corretamente
        self.assertIsInstance(session, StudentSession)
        self.assertEqual(session.student_id, student_id)
        self.assertEqual(session.current_level, "A1")
        self.assertEqual(session.topics_covered, [])
        
    def test_get_session_existing_student(self):
        # Criar uma sessão primeiro
        student_id = "test-student-123"
        session1 = SessionManager.get_session(student_id)
        session1.current_level = "A2"  # Modificar a sessão
        
        # Obter a mesma sessão novamente
        session2 = SessionManager.get_session(student_id)
        
        # Verificar se é a mesma sessão
        self.assertEqual(session1, session2)
        self.assertEqual(session2.current_level, "A2")
        
    def test_student_session_add_interaction(self):
        # Criar uma sessão
        session = StudentSession("test-student-456")
        
        # Adicionar interações
        session.add_interaction("user_message", "Hello")
        session.add_interaction("ai_response", "Hi there")
        
        # Verificar se as interações foram adicionadas
        self.assertEqual(len(session.interactions), 2)
        self.assertEqual(session.interactions[0]["type"], "user_message")
        self.assertEqual(session.interactions[0]["content"], "Hello")
        self.assertEqual(session.interactions[1]["type"], "ai_response")
        self.assertEqual(session.interactions[1]["content"], "Hi there")
        
    def test_student_session_add_topic(self):
        # Criar uma sessão
        session = StudentSession("test-student-789")
        
        # Adicionar tópicos
        session.add_topic("Greetings")
        session.add_topic("Numbers")
        session.add_topic("Greetings")  # Tópico duplicado
        
        # Verificar se os tópicos foram adicionados sem duplicação
        self.assertEqual(len(session.topics_covered), 2)
        self.assertIn("Greetings", session.topics_covered)
        self.assertIn("Numbers", session.topics_covered)
        
    def test_student_session_get_summary(self):
        # Criar uma sessão com dados
        session = StudentSession("test-student-101")
        session.current_level = "B1"
        session.add_topic("Past Tense")
        session.add_interaction("user_message", "How do I use past tense?")
        
        # Obter resumo da sessão
        summary = session.get_session_summary()
        
        # Verificar o resumo
        self.assertEqual(summary["student_id"], "test-student-101")
        self.assertEqual(summary["current_level"], "B1")
        self.assertEqual(summary["topics_covered"], ["Past Tense"])
        self.assertEqual(summary["total_interactions"], 1)
        
    def test_student_session_level_progression(self):
        # Criar uma sessão
        session = StudentSession("test-student-202")
        
        # Simular progresso do aluno
        session.add_topic("Greetings")
        session.add_topic("Numbers")
        session.add_topic("Colors")
        session.add_topic("Family")
        session.add_topic("Food")
        
        # Verificar se o nível foi atualizado (simulação)
        # Na implementação real, isso seria baseado em alguma lógica mais complexa
        session.update_level_based_on_progress()
        
        # Verificar se o nível foi atualizado
        self.assertEqual(session.current_level, "A2")

if __name__ == '__main__':
    unittest.main()