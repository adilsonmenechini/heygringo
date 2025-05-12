# core/routes.py
from flask import Blueprint, jsonify
from vocabulary.contexts import get_vocabulary_by_context, get_all_contexts

api = Blueprint('api', __name__)

@api.route('/vocabulary/<context>')
def get_vocabulary(context):
    """Retorna vocabulário para um contexto específico."""
    vocabulary = get_vocabulary_by_context(context)
    if not vocabulary:
        return jsonify({'error': 'Contexto não encontrado'}), 404
    return jsonify(vocabulary)

@api.route('/vocabulary/contexts')
def get_contexts():
    """Retorna todos os contextos disponíveis."""
    contexts = get_all_contexts()
    return jsonify(contexts)