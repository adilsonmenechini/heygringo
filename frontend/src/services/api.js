// src/services/api.js
const API_BASE_URL = 'http://localhost:5001/api'; // URL do seu backend Python/Flask

export const fetchAIResponse = async (message, history) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message, history }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data.reply;
  } catch (error) {
    console.error("Error fetching AI response:", error);
    return `Desculpe, tive um problema para conectar com a IA: ${error.message}`;
  }
};

export const synthesizeSpeech = async (text, voice = 'en-US-AriaNeural') => {
  try {
    const response = await fetch(`${API_BASE_URL}/tts`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text, voice }),
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
    }
    const audioBlob = await response.blob();
    return URL.createObjectURL(audioBlob); // Cria uma URL para o blob de áudio
  } catch (error) {
    console.error("Error synthesizing speech:", error);
    return null;
  }
};

export const transcribeAudio = async (audioBlob) => {
  try {
    const formData = new FormData();
    formData.append('audio_data', audioBlob, 'recording.wav');

    const response = await fetch(`${API_BASE_URL}/stt`, {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    
    if (!response.ok) {
      throw new Error(data.error || `Erro na transcrição: ${response.status}`);
    }

    if (!data.text) {
      throw new Error('Não foi possível transcrever o áudio. Por favor, tente novamente.');
    }

    return {
      text: data.text,
      pronunciation_score: data.pronunciation_score,
      language_detected: data.language_detected,
      confidence: data.confidence
    };
  } catch (error) {
    console.error("Erro na transcrição do áudio:", error);
    throw new Error(`Erro na transcrição: ${error.message}`);
  }
};