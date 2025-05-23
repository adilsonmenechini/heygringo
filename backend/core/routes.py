# core/routes.py
from flask import Blueprint, jsonify
from vocabulary.contexts import get_vocabulary_by_context, get_all_contexts
from backend.vocabulary.daily_life_lessons import get_all_daily_life_lessons

api = Blueprint('api', __name__) # Existing blueprint for vocabulary

lessons_bp = Blueprint('lessons_api', __name__, url_prefix='/api')

@lessons_bp.route('/lessons', methods=['GET'])
def get_lessons():
    daily_lessons = get_all_daily_life_lessons()
    # For now, just daily_lessons as per example in instructions
    return jsonify(daily_lessons)

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