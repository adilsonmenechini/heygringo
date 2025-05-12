import React, { useState } from 'react';
import './VocabularyCard.css';

const VocabularyCard = ({ word, translation, examples, difficulty }) => {
  const [isFlipped, setIsFlipped] = useState(false);
  const [showExamples, setShowExamples] = useState(false);

  const handleCardClick = () => {
    setIsFlipped(!isFlipped);
  };

  const handleExamplesClick = (e) => {
    e.stopPropagation();
    setShowExamples(!showExamples);
  };

  const difficultyColors = {
    'A1': '#4CAF50',
    'A2': '#8BC34A',
    'B1': '#FFC107',
    'B2': '#FF9800',
    'C1': '#FF5722',
    'C2': '#F44336'
  };

  return (
    <div 
      className={`vocabulary-card ${isFlipped ? 'flipped' : ''}`}
      onClick={handleCardClick}
    >
      <div className="card-inner">
        <div className="card-front">
          <span 
            className="difficulty-badge"
            style={{ backgroundColor: difficultyColors[difficulty] }}
          >
            {difficulty}
          </span>
          <h3>{word}</h3>
          <p className="translation">{translation}</p>
          <button 
            className="examples-button"
            onClick={handleExamplesClick}
          >
            Ver Exemplos
          </button>
        </div>
        <div className="card-back">
          {showExamples && (
            <div className="examples-container">
              <h4>Exemplos:</h4>
              <ul>
                {examples.map((example, index) => (
                  <li key={index}>{example}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default VocabularyCard;