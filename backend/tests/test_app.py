# backend/test_app.py
import unittest
import json
from unittest.mock import patch, MagicMock
from app import app
from session_manager import SessionManager

class TestHeyGringoApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Mock para o modelo Whisper
        self.whisper_patcher = patch('app.whisper_model')
        self.mock_whisper = self.whisper_patcher.start()
        # Mock para o Ollama
        self.ollama_patcher = patch('app.ollama.chat')
        self.mock_ollama = self.ollama_patcher.start()
        # Mock para o SessionManager
        self.session_patcher = patch('app.SessionManager.get_session')
        self.mock_session = self.session_patcher.start()
        
    def tearDown(self):
        self.whisper_patcher.stop()
        self.ollama_patcher.stop()
        self.session_patcher.stop()
    
    def test_chat_endpoint_success(self):
        # Configurar mocks
        mock_session_instance = MagicMock()
        mock_session_instance.current_level = "A1"
        mock_session_instance.topics_covered = ["Greetings"]
        mock_session_instance.get_session_summary.return_value = {"level": "A1"}
        self.mock_session.return_value = mock_session_instance
        
        self.mock_ollama.return_value = {
            'message': {'content': '[EN] Hello! How are you?\n[PT] Olá! Como vai você?'}
        }
        
        # Testar endpoint
        response = self.app.post('/api/chat',
                               data=json.dumps({
                                   'message': 'Olá',
                                   'history': [],
                                   'student_id': '123'
                               }),
                               content_type='application/json')
        
        data = json.loads(response.data)
        
        # Verificações
        self.assertEqual(response.status_code, 200)
        self.assertIn('reply', data)
        self.assertIn('points_earned', data)
        self.assertEqual(mock_session_instance.add_interaction.call_count, 2)  # user_message e ai_response
        
    def test_chat_endpoint_no_message(self):
        response = self.app.post('/api/chat',
                               data=json.dumps({
                                   'message': '',
                                   'student_id': '123'
                               }),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        
    def test_tts_endpoint_success(self):
        with patch('app.subprocess.run') as mock_subprocess:
            with patch('app.tempfile.NamedTemporaryFile') as mock_tempfile:
                mock_tempfile.return_value.__enter__.return_value.name = '/tmp/test.mp3'
                with patch('app.os.path.getsize') as mock_getsize:
                    mock_getsize.return_value = 1024  # Tamanho simulado do arquivo
                    
                    response = self.app.post('/api/tts',
                                          data=json.dumps({
                                              'text': 'Hello',
                                              'voice': 'en-US-AriaNeural'
                                          }),
                                          content_type='application/json')
                    
                    self.assertEqual(response.status_code, 200)
                    mock_subprocess.assert_called_once()
    
    def test_stt_endpoint_success(self):
        # Configurar mock do Whisper
        mock_segments = [MagicMock(text="Hello, how are you?")]
        mock_info = MagicMock(language="en", language_probability=0.95)
        self.mock_whisper.transcribe.return_value = (mock_segments, mock_info)
        
        # Criar um arquivo de teste
        with open('/tmp/test_audio.wav', 'wb') as f:
            f.write(b'test audio content')
            
        with open('/tmp/test_audio.wav', 'rb') as f:
            response = self.app.post('/api/stt',
                                   data={'audio_data': (f, 'test_audio.wav')},
                                   content_type='multipart/form-data')
            
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('text', data)
        self.assertIn('pronunciation_score', data)
        self.assertEqual(data['text'], 'Hello, how are you?')

if __name__ == '__main__':
    unittest.main()