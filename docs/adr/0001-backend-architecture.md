# ADR 0001: Arquitetura do Backend

## Status

Aceito

## Contexto

O projeto requer um backend robusto para gerenciar a lógica de negócios da aplicação de ensino de inglês, incluindo:
- Processamento de requisições dos usuários
- Gerenciamento de sessões
- Integração com modelo de IA (Ollama)
- Processamento de áudio e texto

## Decisão

Decidimos utilizar:
1. **Python com Flask**
   - Framework web leve e flexível (v2.3.x)
   - Fácil integração com diferentes bibliotecas
   - Suporte a RESTful APIs
   - Blueprints para organização modular
   - Flask-CORS para gerenciamento de CORS

2. **Bibliotecas Principais**
   - Whisper (v20231117): Processamento de áudio e transcrição
   - Ollama (v0.1.x): Integração com modelo de IA
   - PyJSON-Logger (v2.0.x): Logging estruturado
   - Python-dotenv (v1.0.x): Gerenciamento de configurações
   - Pytest (v7.4.x): Framework de testes

3. **Arquitetura Modular**
   - Core: Configurações e handlers principais
   - Utils: Utilitários como logging
   - Vocabulary: Gestão de conteúdo didático
   - Tests: Testes automatizados

4. **Gerenciamento de Sessão**
   - Implementação de sistema de sessões personalizado
   - Armazenamento em arquivos JSON para persistência

5. **Sistema de Logging**
   - Logging estruturado em JSON
   - Rotação de logs
   - Separação de logs por nível

## Consequências

### Positivas
- Alta flexibilidade para adaptações
- Fácil manutenção devido à estrutura modular
- Logging robusto para monitoramento
- Testes automatizados facilitam garantia de qualidade

### Negativas
- Necessidade de gerenciar sessões manualmente
- Responsabilidade de escalar horizontalmente quando necessário

## Notas

- A estrutura atual suporta bem o desenvolvimento ágil
- Monitoramento via logs estruturados facilita debugging
- Sistema de sessões permite persistência sem necessidade imediata de banco de dados