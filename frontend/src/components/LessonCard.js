// src/components/LessonCard.js
import React from 'react';
import './LessonCard.css';

const LessonCard = ({ title, description, icon, completed, locked, onSelect }) => {
  const cardClass = `lesson-card ${completed ? 'completed' : ''} ${locked ? 'locked' : ''}`;
  
  return (
    <div 
      className={cardClass}
      onClick={!locked ? onSelect : undefined}
    >
      <div className="lesson-icon">
        {icon}
        {completed && <div className="completion-badge">✓</div>}
        {locked && <div className="lock-badge">🔒</div>}
      </div>
      <div className="lesson-content">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
      {!locked && !completed && (
        <div className="start-button">
          Iniciar
        </div>
      )}
      {completed && (
        <div className="practice-button">
          Praticar
        </div>
      )}
    </div>
  );
};

export default LessonCard;