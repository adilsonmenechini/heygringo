# Projeto Hey Gringo

## 📋 Sobre o Projeto
Este projeto é uma aplicação de ensino de inglês que integra tecnologias modernas para fornecer uma experiência de aprendizado eficiente e interativa.

## 🏗️ Arquitetura

### Backend (Python/Flask)
- **Framework Principal**: Flask v2.3.x
- **Funcionalidades Principais**:
  - Processamento de requisições dos usuários
  - Gerenciamento de sessões
  - Integração com modelo de IA (Ollama)
  - Processamento de áudio e texto

#### Bibliotecas Principais
- Whisper (v20231117): Processamento de áudio e transcrição
- Ollama (v0.1.x): Integração com modelo de IA
- PyJSON-Logger (v2.0.x): Logging estruturado
- Python-dotenv (v1.0.x): Gerenciamento de configurações
- Pytest (v7.4.x): Framework de testes

### Frontend (React)
- **Framework Principal**: React v18.2.x
- **Bibliotecas Principais**:
  - React Router (v6.x): Gerenciamento de rotas
  - React Query (v4.x): Gerenciamento de estado e cache
  - Axios (v1.6.x): Cliente HTTP
  - Zod (v3.x): Validação de esquemas
  - Jest (v29.x): Framework de testes

## 🚀 Características

### Backend
- Arquitetura modular e escalável
- Sistema de logging estruturado em JSON
- Testes automatizados
- Alta flexibilidade para adaptações

### Frontend
- Componentes reutilizáveis
- Web Vitals para monitoramento de performance
- Design responsivo com TailwindCSS
- Testes de componentes com Testing Library

## 📦 Estrutura do Projeto

### Backend
```
backend/
├── core/           # Configurações e handlers principais
├── utils/          # Utilitários como logging
├── vocabulary/     # Gestão de conteúdo didático
└── tests/          # Testes automatizados
```

### Frontend
```
frontend/
├── components/     # Componentes reutilizáveis
├── features/       # Funcionalidades específicas
├── services/       # Integração com backend
└── hooks/          # Lógica reutilizável
```

## 🛠️ Requisitos do Sistema
- Python 3.x
- Node.js (versão LTS)
- NPM ou Yarn

## 🔧 Configuração e Instalação

1. Clone o repositório
```bash
git clone [URL_DO_REPOSITÓRIO]
```

2. Configure o Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure o Frontend
```bash
cd frontend
npm install  # ou yarn install
```

## 🚀 Executando o Projeto

1. Inicie o Backend
```bash
cd backend
flask run
```

2. Inicie o Frontend
```bash
cd frontend
npm start  # ou yarn start
```

## 📝 Notas Adicionais
- A estrutura de componentes facilita manutenção
- Web Vitals ajuda no monitoramento de performance
- Organização por features permite escalabilidade

## 🤝 Contribuindo
Por favor, leia o arquivo CONTRIBUTING.md para detalhes sobre nosso código de conduta e o processo para enviar pull requests.

## 📄 Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE.md para detalhes.