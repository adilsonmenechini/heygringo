// src/components/ProgressBar.js
import React from 'react';
import './ProgressBar.css';

const ProgressBar = ({ progress, level, points, streakDays }) => {
  // Calcula a cor da barra de progresso baseada no nível
  const getProgressColor = () => {
    const colors = [
      '#58cc02', // Verde Duolingo
      '#ce82ff', // Roxo
      '#ff9600', // Laranja
      '#2b70c9', // Azul
      '#ff4b4b'  // Vermelho
    ];
    return colors[level % colors.length];
  };

  return (
    <div className="progress-container">
      <div className="progress-header">
        <div className="level-badge" style={{ backgroundColor: getProgressColor() }}>
          <span>{level}</span>
        </div>
        <div className="progress-info">
          <div className="points">
            <span className="points-icon">💎</span>
            <span>{points} pontos</span>
          </div>
          <div className="streak">
            <span className="streak-icon">🔥</span>
            <span>{streakDays} dias</span>
          </div>
        </div>
      </div>
      <div className="progress-bar-container">
        <div 
          className="progress-bar" 
          style={{ 
            width: `${progress}%`,
            backgroundColor: getProgressColor()
          }}
        ></div>
      </div>
    </div>
  );
};

export default ProgressBar;