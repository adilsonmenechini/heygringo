// src/ChatInput.js
import React, { useState, useRef, useEffect } from 'react';

const ChatInput = ({ onSendMessage, onSendAudio, isLoading }) => {
  const [inputValue, setInputValue] = useState('');
  const [isRecording, setIsRecording] = useState(false);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim() && !isLoading) {
      onSendMessage(inputValue);
      setInputValue('');
    }
  };

  const toggleRecording = async () => {
    if (isRecording) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
      // O evento 'stop' do MediaRecorder cuidará de enviar o áudio
    } else {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorderRef.current = new MediaRecorder(stream);
        audioChunksRef.current = [];

        mediaRecorderRef.current.ondataavailable = (event) => {
          audioChunksRef.current.push(event.data);
        };

        mediaRecorderRef.current.onstop = () => {
          const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/wav' }); // Ou 'audio/webm' dependendo do encoder
          onSendAudio(audioBlob);
          audioChunksRef.current = [];
          // Parar as trilhas do stream para desligar o indicador do microfone
          stream.getTracks().forEach(track => track.stop());
        };

        mediaRecorderRef.current.start();
        setIsRecording(true);
      } catch (err) {
        console.error("Error accessing microphone:", err);
        alert("Erro ao acessar microfone. Verifique as permissões.");
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="chat-input-form">
      <input
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        placeholder={isLoading ? "Aguarde a Hey Gringo!..." : "Digite sua mensagem ou dúvida..."}
        disabled={isLoading || isRecording}
      />
      <button type="button" onClick={toggleRecording} disabled={isLoading} className="mic-button">
        {isRecording ? '🛑' : '🎤'}
      </button>
      <button type="submit" disabled={isLoading || isRecording || !inputValue.trim()}>
        Enviar
      </button>
    </form>
  );
};

export default ChatInput;