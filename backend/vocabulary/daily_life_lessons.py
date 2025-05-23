# backend/vocabulary/daily_life_lessons.py

DAILY_LIFE_LESSONS = [
    {
        'id': 'directions_1',
        'title': 'Pedindo Direções Básicas',
        'description': 'Aprenda a perguntar e entender direções simples em inglês.',
        'icon': '🗺️',
        'scenario_key': 'directions',
        'target_phrases': [
            "Excuse me, how can I get to [place]?",
            "Where is the nearest [place]?",
            "Is it far from here?",
            "Could you show me on the map?",
            "Turn left.",
            "Turn right.",
            "Go straight ahead."
        ],
        'exercises': [
            {'type': 'role_play_prompt', 'prompt': "Você está em uma cidade nova e quer encontrar um museu. Pergunte a um pedestre como chegar lá usando as frases alvo."},
            {'type': 'vocabulary_review', 'context_words': ['left', 'right', 'straight ahead', 'corner', 'map', 'address', 'landmark']},
            {'type': 'phrase_translation', 'items': [
                {'en': "Excuse me, where is the bank?", 'pt': "Com licença, onde fica o banco?"},
                {'en': "Go straight ahead for two blocks, then turn right.", 'pt': "Siga em frente por dois quarteirões, depois vire à direita."}
            ]},
            {'type': 'sentence_completion', 'prompt': "To get to the library, you need to ___ left at the next corner.", 'options': ['turn', 'go', 'stop'], 'answer': 'turn'}
        ]
    },
    {
        'id': 'phone_calls_1',
        'title': 'Fazendo uma Ligação Simples',
        'description': 'Pratique como iniciar e terminar uma ligação telefônica básica em inglês.',
        'icon': '📞',
        'scenario_key': 'phone_calls',
        'target_phrases': [
            "Hello, may I speak to [Name]?",
            "This is [Your Name] speaking.",
            "Could I leave a message?",
            "Thanks for calling.",
            "I'll call back later."
        ],
        'exercises': [
            {'type': 'role_play_prompt', 'prompt': "Você precisa ligar para um amigo para confirmar os planos para o fim de semana. Inicie a conversa e use as frases alvo."},
            {'type': 'vocabulary_match', 'items': [
                {'en': 'call', 'pt': 'ligar/chamada'},
                {'en': 'phone number', 'pt': 'número de telefone'},
                {'en': 'voicemail', 'pt': 'correio de voz'}
            ]},
            {'type': 'multiple_choice_question', 'prompt': "What do you say if the person you want to talk to is not available?", 'options': ["I'll hang up now.", "Could I leave a message?", "Who is this?"], 'answer': "Could I leave a message?"}
        ]
    },
    {
        'id': 'public_transport_1',
        'title': 'Usando Transporte Público',
        'description': 'Aprenda frases essenciais para comprar passagens e perguntar sobre rotas.',
        'icon': '🚌',
        'scenario_key': 'public_transport',
        'target_phrases': [
            "A ticket to [destination], please.",
            "Which platform for the train to [destination]?",
            "What time is the next bus to [place]?",
            "Does this bus go to [place]?",
            "How much is the fare?"
        ],
        'exercises': [
            {'type': 'role_play_prompt', 'prompt': "Você está em uma estação de trem e precisa comprar uma passagem para o aeroporto. Use as frases alvo para interagir com o bilheteiro."},
            {'type': 'vocabulary_review', 'context_words': ['bus', 'train', 'subway', 'ticket', 'platform', 'stop', 'fare', 'route', 'schedule']},
            {'type': 'phrase_translation', 'items': [
                {'en': "A one-way ticket to downtown, please.", 'pt': "Uma passagem só de ida para o centro, por favor."},
                {'en': "What time does the next train arrive?", 'pt': "A que horas chega o próximo trem?"}
            ]}
        ]
    },
    {
        'id': 'health_1',
        'title': 'Interações Básicas de Saúde',
        'description': 'Aprenda a descrever sintomas simples e interagir em uma farmácia.',
        'icon': '⚕️', # Alt icon for health
        'scenario_key': 'health',
        'target_phrases': [
            "I have a [symptom].",
            "I need something for a [symptom].",
            "I'd like to make an appointment to see a doctor.",
            "How often should I take this medicine?",
            "Do I need a prescription for this?"
        ],
        'exercises': [
            {'type': 'role_play_prompt', 'prompt': "Você não está se sentindo bem e vai à farmácia. Descreva seus sintomas (dor de cabeça e tosse) e peça um remédio."},
            {'type': 'vocabulary_match', 'items': [
                {'en': 'headache', 'pt': 'dor de cabeça'},
                {'en': 'pharmacy', 'pt': 'farmácia'},
                {'en': 'prescription', 'pt': 'receita médica'}
            ]},
            {'type': 'sentence_completion', 'prompt': "If you have a fever and a cough, you might have the ___.", 'options': ['flu', 'pain', 'appointment'], 'answer': 'flu'}
        ]
    },
    {
        'id': 'social_talk_1',
        'title': 'Conversa Social Básica',
        'description': 'Pratique como iniciar e manter conversas leves sobre tópicos do dia a dia.',
        'icon': '💬',
        'scenario_key': 'social_talk',
        'target_phrases': [
            "How are you doing?",
            "Nice weather today, isn't it?",
            "What did you do over the weekend?",
            "How's work/studies going?",
            "Do you have any hobbies?"
        ],
        'exercises': [
            {'type': 'role_play_prompt', 'prompt': "Você encontra um colega no café. Inicie uma conversa social usando uma das frases alvo e tente manter o diálogo."},
            {'type': 'vocabulary_review', 'context_words': ['weather', 'hobbies', 'weekend', 'work', 'studies', 'news', 'movie']},
            {'type': 'multiple_choice_question', 'prompt': "A common way to start a conversation with someone you don't know well is to talk about the ___.", 'options': ['politics', 'weather', 'personal problems'], 'answer': 'weather'}
        ]
    }
]

def get_all_daily_life_lessons() -> list:
    """Retorna toda a lista DAILY_LIFE_LESSONS."""
    return DAILY_LIFE_LESSONS

def get_daily_life_lesson_by_id(lesson_id: str) -> dict | None:
    """Retorna uma lição específica da lista DAILY_LIFE_LESSONS pelo ID, ou None se não encontrada."""
    for lesson in DAILY_LIFE_LESSONS:
        if lesson['id'] == lesson_id:
            return lesson
    return None
