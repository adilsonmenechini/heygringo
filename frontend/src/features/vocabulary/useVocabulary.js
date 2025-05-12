import { useState, useEffect } from 'react';

export const useVocabulary = (initialContext = 'supermercado') => {
  const [context, setContext] = useState(initialContext);
  const [vocabulary, setVocabulary] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedDifficulty, setSelectedDifficulty] = useState(null);
  const [filteredVocabulary, setFilteredVocabulary] = useState([]);

  useEffect(() => {
    fetchVocabulary();
  }, [context]);

  useEffect(() => {
    filterVocabulary();
  }, [vocabulary, selectedDifficulty]);

  const filterVocabulary = () => {
    if (!selectedDifficulty) {
      setFilteredVocabulary(vocabulary);
    } else {
      const filtered = vocabulary.filter(word => word.difficulty === selectedDifficulty);
      setFilteredVocabulary(filtered);
    }
  };

  const fetchVocabulary = async () => {
    try {
      setLoading(true);
      const response = await fetch(`/api/vocabulary/${context}`);
      const data = await response.json();
      setVocabulary(data);
    } catch (error) {
      console.error('Erro ao carregar vocabulário:', error);
    } finally {
      setLoading(false);
    }
  };

  return {
    context,
    setContext,
    vocabulary: filteredVocabulary,
    loading,
    selectedDifficulty,
    setSelectedDifficulty
  };
};