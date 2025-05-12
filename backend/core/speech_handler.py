# core/speech_handler.py
from flask import jsonify, send_file
from utils.logger import info, error, debug, warning
import tempfile
import os
import time
import subprocess
from faster_whisper import WhisperModel
import traceback

class SpeechHandler:
    def __init__(self):
        self.whisper_model = None
        self.initialize_whisper_model()

    def initialize_whisper_model(self):
        try:
            info("Iniciando carregamento do modelo faster-whisper")
            start_time = time.time()
            self.whisper_model = WhisperModel("base", device="cpu", compute_type="int8")
            load_time = time.time() - start_time
            info("Modelo faster-whisper carregado com sucesso", load_time_seconds=load_time)
        except Exception as e:
            error("Erro ao carregar modelo whisper", exception=str(e), traceback=traceback.format_exc())
            self.whisper_model = None

    def text_to_speech(self, text, voice='en-US-AriaNeural'):
        if not text:
            warning("Requisição TTS sem texto")
            return jsonify({"error": "No text provided"}), 400

        try:
            debug("Iniciando síntese de voz", 
                  voice=voice, 
                  text_length=len(text))
            
            # Usar um arquivo temporário para o áudio
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp_audio_file:
                tmp_filename = tmp_audio_file.name

            # Comando para edge-tts
            start_time = time.time()
            subprocess.run(
                ['edge-tts', '--text', text, '--voice', voice, '--write-media', tmp_filename],
                check=True
            )
            synthesis_time = time.time() - start_time
            
            info("Síntese de voz concluída", 
                 synthesis_time_seconds=synthesis_time,
                 audio_file_size=os.path.getsize(tmp_filename))
            
            return tmp_filename

        except subprocess.CalledProcessError as e:
            error("Erro no edge-tts", 
                  exception=str(e),
                  command=e.cmd,
                  returncode=e.returncode,
                  output=e.output if hasattr(e, 'output') else None)
            if os.path.exists(tmp_filename):
                os.remove(tmp_filename)
            return jsonify({"error": f"edge-tts failed: {e}"}), 500
        except Exception as e:
            error("Erro geral no TTS", 
                  exception=str(e),
                  traceback=traceback.format_exc())
            if os.path.exists(tmp_filename):
                os.remove(tmp_filename)
            return jsonify({"error": str(e)}), 500

    def speech_to_text(self, audio_file, student_id='unknown'):
        if not self.whisper_model:
            error("Whisper model not initialized", student_id=student_id)
            return jsonify({"error": "Speech recognition service is unavailable"}), 503

        temp_audio_path = None
        try:
            # Salvar o arquivo de áudio temporariamente
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_audio:
                audio_file.save(tmp_audio.name)
                temp_audio_path = tmp_audio.name
            
            file_size = os.path.getsize(temp_audio_path)
            debug("Arquivo de áudio recebido", 
                  student_id=student_id, 
                  file_size_bytes=file_size,
                  file_path=temp_audio_path)
            
            # Transcrever usando faster-whisper
            start_time = time.time()
            try:
                transcription_result = self.whisper_model.transcribe(temp_audio_path, task="transcribe")
                segments = list(transcription_result[0])  # Converter generator para lista
                whisper_info = transcription_result[1]
                transcription_time = time.time() - start_time
                
                if not segments:
                    raise ValueError("Nenhum segmento de áudio foi transcrito")
                    
                transcribed_text = " ".join([segment.text for segment in segments])
                
                if not transcribed_text.strip():
                    raise ValueError("Transcrição resultou em texto vazio")
                
                # Log transcription details safely
                log_details = {
                    "student_id": student_id,
                    "transcription_time_seconds": transcription_time,
                    "text_length": len(transcribed_text),
                    "language": whisper_info.language,
                    "language_probability": whisper_info.language_probability,
                    "segments_count": len(segments)
                }
                info("Transcrição de áudio concluída com sucesso", **log_details)
                
                # Calcular pontuação de pronúncia (simulada)
                pronunciation_score = min(whisper_info.language_probability * 100, 100)
                
                return jsonify({
                    "text": transcribed_text,
                    "pronunciation_score": pronunciation_score,
                    "language_detected": whisper_info.language,
                    "confidence": whisper_info.language_probability
                })
            except Exception as transcription_error:
                error("Erro durante a transcrição do áudio", 
                      error_type=type(transcription_error).__name__,
                      error_message=str(transcription_error))
                raise
        except Exception as e:
            error_details = {
                "student_id": student_id,
                "exception": str(e),
                "traceback": traceback.format_exc()
            }
            error("Erro na transcrição de áudio", **error_details)
            return jsonify({"error": str(e)}), 500
        finally:
            # Limpar arquivo temporário
            if temp_audio_path and os.path.exists(temp_audio_path):
                try:
                    os.remove(temp_audio_path)
                    debug("Arquivo temporário de áudio removido", filename=temp_audio_path)
                except OSError as cleanup_error:
                    warning("Erro ao remover arquivo temporário", 
                           filename=temp_audio_path, 
                           exception=str(cleanup_error))