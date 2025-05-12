// src/App.js
import React, { useState, useEffect, useRef } from 'react';
import ChatMessage from './ChatMessage';
import ChatInput from './ChatInput';
import StudentLogin from './components/StudentLogin';
import ProgressBar from './components/ProgressBar';
import LessonCard from './components/LessonCard';
import RewardFeedback from './components/RewardFeedback';
import { fetchAIResponse, synthesizeSpeech, transcribeAudio } from './services/api';
import './App.css';



function App() {
  const [student, setStudent] = useState(null);
  const [messages, setMessages] = useState([]);
  const [userLevel, setUserLevel] = useState(1);
  const [userPoints, setUserPoints] = useState(0);
  const [userStreak, setUserStreak] = useState(1);
  const [progress, setProgress] = useState(30); // Progresso na lição atual (0-100)
  const [showReward, setShowReward] = useState(false);
  const [rewardInfo, setRewardInfo] = useState({ type: '', message: '', points: 0 });
  const [showLessons, setShowLessons] = useState(false); // Para alternar entre chat e lições
  
  useEffect(() => {
    if (student) {
      setMessages([
        { 
          sender: 'ai', 
          text: `Olá ${student.name}! Sou a Hey Gringo!, sua parceira pra desenrolar no inglês. Bora começar? Manda sua primeira dúvida ou só um 'oi'!` 
        }
      ]);
    }
  }, [student]);
  
  const [isLoading, setIsLoading] = useState(false);
  const [autoPlayAudio, setAutoPlayAudio] = useState(true); // Estado para auto-play (ativado por padrão)
  const audioPlayerRef = useRef(null); // Para tocar o áudio TTS
  const chatEndRef = useRef(null); // Para scrollar para o final

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const addMessage = (sender, text) => {
    setMessages(prev => [...prev, { sender, text }]);
  };

  const handleSendMessage = async (userInput) => {
    if (!userInput.trim()) return;
    addMessage('user', userInput);
    setIsLoading(true);

    // Prepara histórico para a API (apenas os últimos N, por exemplo)
    const chatHistoryForApi = messages.slice(-10).map(msg => ({
        sender: msg.sender,
        text: msg.text
    }));

    try {
      const response = await fetchAIResponse(userInput, chatHistoryForApi);
      // Verifica se a resposta é um objeto com a propriedade reply ou apenas texto
      const aiReplyText = typeof response === 'object' && response.reply ? response.reply : response;
      addMessage('ai', aiReplyText);
      
      // Atualizar pontos e mostrar recompensa
      const pointsEarned = typeof response === 'object' && response.points_earned ? response.points_earned : 5;
      const newPoints = userPoints + pointsEarned;
      setUserPoints(newPoints);
      
      // Verificar se subiu de nível (a cada 100 pontos)
      if (Math.floor(newPoints / 100) > Math.floor(userPoints / 100)) {
        const newLevel = userLevel + 1;
        setUserLevel(newLevel);
        setShowReward(true);
        setRewardInfo({
          type: 'level-up',
          message: `Parabéns! Você alcançou o nível ${newLevel}!`,
          points: pointsEarned
        });
      } else {
        setShowReward(true);
        setRewardInfo({
          type: 'points',
          message: 'Ótimo trabalho!',
          points: pointsEarned
        });
      }
      
      // Atualizar progresso na lição
      setProgress(prev => Math.min(prev + 10, 100));
      
      if (autoPlayAudio) {
        handlePlayAudio(aiReplyText);
      }
    } catch (error) {
      console.error('Erro ao processar mensagem:', error);
      addMessage('ai', 'Desculpe, ocorreu um erro ao processar sua mensagem.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleSendAudio = async (audioBlob) => {
    setIsLoading(true);
    addMessage('user', "[Audio sendo processado... 🎙️]"); // Feedback para o usuário
    
    try {
      const response = await transcribeAudio(audioBlob);
      
      // Remove a mensagem de "Audio sendo processado" e adiciona a transcrição
      setMessages(prev => prev.slice(0, -1)); 
  
      if (response && (typeof response === 'string' || response.text)) {
        const transcribedText = typeof response === 'string' ? response : response.text;
        addMessage('user', transcribedText + " (🎤)");
        
        // Mostrar feedback de pronúncia se disponível
        if (typeof response === 'object' && response.pronunciation_score) {
          const score = response.pronunciation_score;
          let rewardType = 'correct';
          let message = 'Excelente pronúncia!';
          
          if (score < 70) {
            rewardType = 'incorrect';
            message = 'Continue praticando sua pronúncia!';
          } else if (score < 90) {
            rewardType = 'points';
            message = 'Boa pronúncia!';
          }
          
          setShowReward(true);
          setRewardInfo({
            type: rewardType,
            message: message,
            points: Math.floor(score / 10)
          });
          
          // Adicionar pontos baseados na pronúncia
          setUserPoints(prev => prev + Math.floor(score / 10));
        }
        
        // Prepara histórico para a API
        const chatHistoryForApi = messages.slice(-10).map(msg => ({
            sender: msg.sender,
            text: msg.text
        }));
        
        const aiResponse = await fetchAIResponse(transcribedText, chatHistoryForApi);
        const aiReplyText = typeof aiResponse === 'object' && aiResponse.reply ? aiResponse.reply : aiResponse;
        addMessage('ai', aiReplyText);
        
        if (autoPlayAudio) {
          handlePlayAudio(aiReplyText);
        }
        
        // Atualizar progresso
        setProgress(prev => Math.min(prev + 15, 100));
      } else {
        addMessage('ai', "Desculpe, não consegui entender o áudio. Tente falar mais claro ou verifique seu microfone.");
      }
    } catch (error) {
      console.error('Erro ao processar áudio:', error);
      setMessages(prev => prev.slice(0, -1)); // Remove mensagem de processamento
      addMessage('ai', "Ocorreu um erro ao processar seu áudio. Por favor, tente novamente.");
    } finally {
      setIsLoading(false);
    }
  };

  const handlePlayAudio = async (textToSpeak) => {
    if (!textToSpeak) return;
    setIsLoading(true); // Pode usar um estado específico para "speaking"
    const audioUrl = await synthesizeSpeech(textToSpeak);
    setIsLoading(false);
    if (audioUrl && audioPlayerRef.current) {
      audioPlayerRef.current.src = audioUrl;
      audioPlayerRef.current.play()
        .catch(e => console.error("Error playing audio:", e));
    } else if (!audioUrl) {
      console.warn("Não foi possível gerar o áudio para:", textToSpeak);
    }
  };

  const handleLogin = (studentData) => {
    setStudent(studentData);
    // Aqui você pode adicionar lógica para inicializar a sessão do aluno
  };

  // Função para lidar com o fechamento do feedback de recompensa
  const handleCloseReward = () => {
    setShowReward(false);
  };
  
  // Função para alternar entre chat e lições
  const toggleView = () => {
    setShowLessons(!showLessons);
  };
  
  // Dados de exemplo para as lições
  const lessonData = [
    {
      title: "Saudações Básicas",
      description: "Aprenda a se apresentar e cumprimentar pessoas",
      icon: "👋",
      completed: progress === 100,
      locked: false
    },
    {
      title: "No Café",
      description: "Vocabulário para pedir bebidas e comidas",
      icon: "☕",
      completed: false,
      locked: progress < 100
    },
    {
      title: "Fazendo Compras",
      description: "Como comprar itens e perguntar preços",
      icon: "🛒",
      completed: false,
      locked: progress < 100
    }
  ];
  
  if (!student) {
    return <StudentLogin onLogin={handleLogin} />;
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Hey Gringo! <span role="img" aria-label="Brazil flag">🇧🇷</span>➡️<span role="img" aria-label="USA flag">🇺🇸</span> Teacher</h1>
        <div className="student-info">
          <p>Aluno: {student.name} {student.id ? `(ID: ${student.id})` : ''}</p>
        </div>
        <div className="view-toggle" onClick={toggleView}>
          {showLessons ? "Ver Chat" : "Ver Lições"}
        </div>
        <div className="autoplay-controls">
          <label htmlFor="autoplay-checkbox">
            Reproduzir áudio da IA automaticamente:
          </label>
          <input
            type="checkbox"
            id="autoplay-checkbox"
            checked={autoPlayAudio}
            onChange={(e) => setAutoPlayAudio(e.target.checked)}
          />
        </div>
      </header>
      
      {/* Barra de progresso estilo Duolingo */}
      <ProgressBar 
        progress={progress} 
        level={userLevel} 
        points={userPoints} 
        streakDays={userStreak} 
      />
      
      {showLessons ? (
        <div className="lessons-container">
          <h2>Suas Lições</h2>
          {lessonData.map((lesson, index) => (
            <LessonCard 
              key={index}
              title={lesson.title}
              description={lesson.description}
              icon={lesson.icon}
              completed={lesson.completed}
              locked={lesson.locked}
              onSelect={() => {
                setShowLessons(false); // Voltar para o chat ao selecionar uma lição
                if (!lesson.completed && !lesson.locked) {
                  addMessage('ai', `Vamos praticar "${lesson.title}"! O que você gostaria de saber?`);
                }
              }}
            />
          ))}
        </div>
      ) : (
        <div className="chat-container">
          <div className="chat-messages">
            {messages.map((msg, index) => (
              <ChatMessage
                key={index}
                sender={msg.sender}
                text={msg.text}
                onPlayAudio={msg.sender === 'ai' ? handlePlayAudio : null}
              />
            ))}
            {isLoading && <div className="chat-message ai-message typing-indicator">Hey Gringo! está digitando...</div>}
            <div ref={chatEndRef} />
          </div>
          <ChatInput 
              onSendMessage={handleSendMessage} 
              onSendAudio={handleSendAudio}
              isLoading={isLoading} 
          />
        </div>
      )}
      
      <audio ref={audioPlayerRef} style={{ display: 'none' }} />
      
      {/* Componente de feedback de recompensa */}
      {showReward && (
        <RewardFeedback 
          show={showReward}
          type={rewardInfo.type}
          message={rewardInfo.message}
          points={rewardInfo.points}
          onClose={handleCloseReward}
        />
      )}
      
      <footer>
        <p>Powered by Ollama, edge-tts, faster-whisper & React</p>
      </footer>
    </div>
  );
}

export default App;