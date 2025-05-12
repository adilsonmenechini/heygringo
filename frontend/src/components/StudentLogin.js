// src/components/StudentLogin.js
import React, { useState } from 'react';
import './StudentLogin.css';

const StudentLogin = ({ onLogin }) => {
  const [studentId, setStudentId] = useState('');
  const [studentName, setStudentName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (studentId.trim() || studentName.trim()) {
      onLogin({ id: studentId.trim() || null, name: studentName.trim() || null });
    }
  };

  return (
    <div className="student-login">
      <div className="login-container">
        <h2>Bem-vindo(a) ao Hey Gringo!</h2>
        <p>Por favor, identifique-se para começar</p>
        
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <input
              type="text"
              value={studentId}
              onChange={(e) => setStudentId(e.target.value)}
              placeholder="ID do Aluno (opcional)"
              className="login-input"
            />
          </div>
          
          <div className="input-group">
            <input
              type="text"
              value={studentName}
              onChange={(e) => setStudentName(e.target.value)}
              placeholder="Nome do Aluno"
              className="login-input"
              required
            />
          </div>
          
          <button type="submit" className="login-button">
            Começar Aula
          </button>
        </form>
      </div>
    </div>
  );
};

export default StudentLogin;