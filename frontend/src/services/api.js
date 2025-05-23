// src/services/api.js
const API_BASE_URL = 'http://localhost:5001/api'; // URL do seu backend Python/Flask

export const fetchLessons = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/lessons`);
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching lessons:", error);
    throw error; // Re-throw to allow caller to handle
  }
};

export const fetchAIResponse = async (message, history, student_id, scenario = null) => {
  const payload = {
    message: message,
    history: history,
    student_id: student_id // Added student_id
  };

  if (scenario) {
    payload.current_scenario = scenario; // Conditionally add scenario
  }

  try {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload), // Use the constructed payload
    });
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    // The backend now returns a more complex object, not just data.reply
    // For now, let's assume App.js will handle the new structure, so return full data.
    return data; 
  } catch (error) {
    console.error("Error fetching AI response:", error);
    // Let's re-throw the error so App.js can handle it, e.g. display a message
    throw error; 
    // Old: return `Desculpe, tive um problema para conectar com a IA: ${error.message}`;
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