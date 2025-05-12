import React from 'react';
import VocabularyCard from './VocabularyCard';
import DifficultyFilter from './DifficultyFilter';
import { useVocabulary } from './useVocabulary';
import { VOCABULARY_CONTEXTS } from './config';
import './VocabularyContext.css';

const VocabularyContext = () => {
  const {
    context,
    setContext,
    vocabulary,
    loading,
    selectedDifficulty,
    setSelectedDifficulty
  } = useVocabulary();

  const handleContextChange = (newContext) => {
    setContext(newContext);
  };

  return (
    <div className="vocabulary-context">
      <div className="context-selector">
        {VOCABULARY_CONTEXTS.map((ctx) => (
          <button
            key={ctx.id}
            className={`context-button ${context === ctx.id ? 'active' : ''}`}
            onClick={() => handleContextChange(ctx.id)}
          >
            {ctx.label}
          </button>
        ))}
      </div>

      <DifficultyFilter
        selectedDifficulty={selectedDifficulty}
        onDifficultyChange={setSelectedDifficulty}
      />

      {loading ? (
        <div className="loading-spinner">Carregando...</div>
      ) : (
        <div className="vocabulary-grid">
          {vocabulary.map((word, index) => (
            <VocabularyCard
              key={index}
              word={word.word}
              translation={word.translation}
              examples={word.examples}
              difficulty={word.difficulty}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default VocabularyContext;