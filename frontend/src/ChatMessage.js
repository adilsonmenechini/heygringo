// src/ChatMessage.js
import React from 'react';

const ChatMessage = ({ sender, text, onPlayAudio }) => {
  const isAI = sender === 'ai';

  // Simples parser para [EN], [PT], [Explicação]
  const parseMessage = (rawText) => {
    if (!rawText || typeof rawText !== 'string') return [{ type: 'plain', content: rawText || '' }];

    const parts = [];
    // Added 'Tip' and 'Dica' to the regex
    const regex = /\[(EN|PT|Explicação|Tip|Dica)\]\s*([\s\S]*?)(?=\n\[(EN|PT|Explicação|Tip|Dica)\]|$)/gi;
    let match;
    let lastIndex = 0;

    while ((match = regex.exec(rawText)) !== null) {
      // Texto antes do match atual
      if (match.index > lastIndex) {
        parts.push({ type: 'plain', content: rawText.substring(lastIndex, match.index) });
      }
      let type = match[1].toLowerCase();
      // Normalize 'dica' to 'tip'
      if (type === 'dica') {
        type = 'tip';
      }
      const content = match[2].trim();
      parts.push({ type, content });
      lastIndex = regex.lastIndex;
    }
    // Texto restante após o último match
    if (lastIndex < rawText.length) {
      parts.push({ type: 'plain', content: rawText.substring(lastIndex) });
    }
    
    return parts.length > 0 ? parts : [{ type: 'plain', content: rawText }];
  };

  const messageParts = parseMessage(text);

  return (
    <div className={`chat-message ${isAI ? 'ai-message' : 'user-message'}`}>
      {messageParts.map((part, index) => {
        if (part.type === 'en') {
          return <p key={index} className="lang-en" style={{ whiteSpace: 'pre-line' }}><strong>[EN]</strong> {part.content}</p>;
        } else if (part.type === 'pt') {
          return <p key={index} className="lang-pt" style={{ whiteSpace: 'pre-line' }}><strong>[PT]</strong> {part.content}</p>;
        } else if (part.type === 'explicação') {
          return <p key={index} className="explanation" style={{ whiteSpace: 'pre-line' }}><em>[Explicação]</em> {part.content}</p>;
        } else if (part.type === 'tip') { // Added case for 'tip'
          return <p key={index} className="tip-message" style={{ whiteSpace: 'pre-line' }}><strong>💡 Dica:</strong> {part.content}</p>;
        }
        // Preserva quebras de linha no texto simples
        return <p key={index} style={{ whiteSpace: 'pre-line' }}>{part.content}</p>; // Plain text or unparsed
      })}
      {isAI && onPlayAudio && (
        <button onClick={() => onPlayAudio(text)} className="play-audio-btn">
          🔊 Ouvir
        </button>
      )}
    </div>
  );
};

export default ChatMessage;