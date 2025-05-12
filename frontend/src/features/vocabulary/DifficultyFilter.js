import React from 'react';
import './DifficultyFilter.css';

const DifficultyFilter = ({ selectedDifficulty, onDifficultyChange }) => {
  const difficulties = ['A1', 'A2', 'B1', 'B2'];

  return (
    <div className="difficulty-filter">
      <button
        className={`filter-button ${!selectedDifficulty ? 'active' : ''}`}
        onClick={() => onDifficultyChange(null)}
      >
        Todos
      </button>
      {difficulties.map((difficulty) => (
        <button
          key={difficulty}
          className={`filter-button ${selectedDifficulty === difficulty ? 'active' : ''}`}
          onClick={() => onDifficultyChange(difficulty)}
        >
          {difficulty}
        </button>
      ))}
    </div>
  );
};

export default DifficultyFilter;