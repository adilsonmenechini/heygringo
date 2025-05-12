# backend/logger.py
import logging
import os
import json
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Configuração de diretórios
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Configuração do logger principal
logger = logging.getLogger('hey_gringo')
logger.setLevel(logging.DEBUG)

# Formato para logs de console
console_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Formato para logs de arquivo (mais detalhado)
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

# Handler para console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)

# Handler para arquivo de log geral (rotativo, máximo 5MB, mantém 5 backups)
file_handler = RotatingFileHandler(
    os.path.join(LOG_DIR, 'app.log'),
    maxBytes=5*1024*1024,  # 5MB
    backupCount=5
)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)

# Handler para erros (separado)
error_handler = RotatingFileHandler(
    os.path.join(LOG_DIR, 'error.log'),
    maxBytes=5*1024*1024,  # 5MB
    backupCount=5
)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(file_formatter)

# Adicionar handlers ao logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(error_handler)

# Função para logs estruturados (formato JSON)
def log_structured(level, message, **kwargs):
    """Gera logs estruturados em formato JSON com metadados adicionais."""
    log_data = {
        'timestamp': datetime.now().isoformat(),
        'message': message,
        **kwargs
    }
    
    log_json = json.dumps(log_data)
    
    if level == 'debug':
        logger.debug(log_json)
    elif level == 'info':
        logger.info(log_json)
    elif level == 'warning':
        logger.warning(log_json)
    elif level == 'error':
        logger.error(log_json)
    elif level == 'critical':
        logger.critical(log_json)

# Funções de conveniência para diferentes níveis de log
def debug(message, **kwargs):
    log_structured('debug', message, **kwargs)

def info(message, **kwargs):
    log_structured('info', message, **kwargs)

def warning(message, **kwargs):
    log_structured('warning', message, **kwargs)

def error(message, **kwargs):
    log_structured('error', message, **kwargs)

def critical(message, **kwargs):
    log_structured('critical', message, **kwargs)