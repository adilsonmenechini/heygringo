// src/components/RewardFeedback.js
import React, { useState, useEffect } from 'react';
import './RewardFeedback.css';

const RewardFeedback = ({ show, type, message, points, onClose }) => {
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    if (show) {
      setVisible(true);
      // Fecha automaticamente após 3 segundos
      const timer = setTimeout(() => {
        setVisible(false);
        if (onClose) onClose();
      }, 3000);
      return () => clearTimeout(timer);
    }
  }, [show, onClose]);

  if (!visible) return null;

  const getIcon = () => {
    switch (type) {
      case 'correct':
        return '✅';
      case 'incorrect':
        return '❌';
      case 'level-up':
        return '🏆';
      case 'streak':
        return '🔥';
      case 'points':
        return '💎';
      default:
        return '🎉';
    }
  };

  const getBackgroundColor = () => {
    switch (type) {
      case 'correct':
        return '#58cc02'; // Verde Duolingo
      case 'incorrect':
        return '#ff4b4b'; // Vermelho
      case 'level-up':
        return '#ce82ff'; // Roxo
      case 'streak':
        return '#ff9600'; // Laranja
      case 'points':
        return '#1cb0f6'; // Azul
      default:
        return '#58cc02';
    }
  };

  return (
    <div 
      className="reward-feedback"
      style={{ backgroundColor: getBackgroundColor() }}
    >
      <div className="reward-icon">{getIcon()}</div>
      <div className="reward-message">{message}</div>
      {points && (
        <div className="reward-points">+{points} pontos</div>
      )}
    </div>
  );
};

export default RewardFeedback;