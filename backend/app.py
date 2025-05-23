# backend/app.py
from flask import Flask, request, jsonify, send_file, after_this_request
from flask_cors import CORS
from core.chat_handler import handle_chat_request
from core.speech_handler import SpeechHandler
from core.config import FLASK_CONFIG, TTS_CONFIG
from core.routes import api, lessons_bp # Added lessons_bp
from utils.logger import info, error, debug, warning
import os
import time
import traceback

app = Flask(__name__)
CORS(app)  # Para permitir requisições do frontend React

# Registrar blueprint da API
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(lessons_bp) # Registering the new lessons_bp

# Inicializar o manipulador de fala
speech_handler = SpeechHandler()

# Configuração de logs para requisições HTTP
@app.before_request
def before_request():
    info("Requisição recebida", 
         endpoint=request.endpoint, 
         method=request.method,
         path=request.path,
         remote_addr=request.remote_addr)

@app.after_request
def after_request(response):
    info("Resposta enviada", 
         endpoint=request.endpoint, 
         method=request.method,
         path=request.path,
         status_code=response.status_code)
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    error("Erro não tratado", 
          exception=str(e), 
          traceback=traceback.format_exc(),
          endpoint=request.endpoint,
          method=request.method,
          path=request.path)
    return jsonify({"error": "Ocorreu um erro interno no servidor"}), 500



@app.route('/api/chat', methods=['POST'])
def handle_chat():
    return handle_chat_request(request.json)

@app.route('/api/tts', methods=['POST'])
def text_to_speech():
    data = request.json
    text_to_speak = data.get('text')
    voice = data.get('voice', 'en-US-AriaNeural')

    if not text_to_speak:
        warning("Requisição TTS sem texto")
        return jsonify({"error": "No text provided"}), 400

    try:
        tmp_filename = speech_handler.text_to_speech(text_to_speak, voice)
        
        @after_this_request
        def cleanup(response):
            try:
                time.sleep(0.1)  # Aguardar um pouco para garantir que o arquivo foi enviado
                if os.path.exists(tmp_filename):
                    os.remove(tmp_filename)
                    debug("Arquivo temporário de áudio removido", filename=tmp_filename)
            except OSError as e:
                warning("Não foi possível remover arquivo temporário de áudio", 
                       filename=tmp_filename, 
                       exception=str(e))
            return response

        return send_file(tmp_filename, mimetype='audio/mpeg', as_attachment=True, download_name='speech.mp3')
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/stt', methods=['POST'])
def speech_to_text():
    student_id = request.form.get('student_id', 'unknown')
    
    if 'audio_data' not in request.files:
        warning("Requisição STT sem arquivo de áudio", student_id=student_id)
        return jsonify({"error": "No audio file part"}), 400
    
    file = request.files['audio_data']
    if file.filename == '':
        warning("Requisição STT com nome de arquivo vazio", student_id=student_id)
        return jsonify({"error": "No selected file"}), 400

    return speech_handler.speech_to_text(file, student_id)


if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Rodar em uma porta diferente da do React