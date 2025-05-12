# Módulo de vocabulário para saudações

class Greetings:
    def __init__(self):
        self.greetings = [
            {
                'text': 'Hello',
                'translation': 'Olá',
                'usage_example': 'Hello, how are you?',
                'difficulty': 'beginner',
                'pronunciation_tips': 'he-LOH',
                'common_mistakes': ['Dropping the "h" sound']
            },
            {
                'text': 'Good morning',
                'translation': 'Bom dia',
                'usage_example': 'Good morning! Did you sleep well?',
                'difficulty': 'beginner',
                'pronunciation_tips': 'gud MOR-ning',
                'common_mistakes': ['Pronouncing "morning" as "mourning"']
            },
            {
                'text': 'Good afternoon',
                'translation': 'Boa tarde',
                'usage_example': 'Good afternoon! Nice to meet you.',
                'difficulty': 'beginner',
                'pronunciation_tips': 'gud af-ter-NOON',
                'common_mistakes': ['Skipping the "r" in "afternoon"']
            },
            {
                'text': 'Good evening',
                'translation': 'Boa noite (ao chegar)',
                'usage_example': 'Good evening! Welcome to our party.',
                'difficulty': 'beginner',
                'pronunciation_tips': 'gud EE-vning',
                'common_mistakes': ['Pronouncing "evening" as "even-ing"']
            },
            {
                'text': 'Good night',
                'translation': 'Boa noite (ao se despedir)',
                'usage_example': 'Good night! Sweet dreams.',
                'difficulty': 'beginner',
                'pronunciation_tips': 'gud NAIT',
                'common_mistakes': ['Not distinguishing between "night" and "evening"']
            },
            {
                'text': 'Hi',
                'translation': 'Oi',
                'usage_example': 'Hi! Nice to see you!',
                'difficulty': 'beginner',
                'pronunciation_tips': 'HAI',
                'common_mistakes': ['Pronouncing it too softly']
            },
            {
                'text': 'Hey',
                'translation': 'Ei',
                'usage_example': "Hey! What's up?",
                'difficulty': 'beginner',
                'pronunciation_tips': 'HEY',
                'common_mistakes': ['Making it sound like "hay"']
            },
            {
                'text': "What's up",
                'translation': 'E aí',
                'usage_example': "What's up, how's it going?",
                'difficulty': 'intermediate',
                'pronunciation_tips': 'wuts-UP',
                'common_mistakes': ['Pronouncing "what" formally']
            },
            {
                'text': "How's it going",
                'translation': 'Como vai',
                'usage_example': "How's it going with your new job?",
                'difficulty': 'intermediate',
                'pronunciation_tips': 'hows-it-GO-ing',
                'common_mistakes': ['Not linking the words together']
            },
            {
                'text': 'Nice to meet you',
                'translation': 'Prazer em conhecê-lo(a)',
                'usage_example': 'Hello, nice to meet you!',
                'difficulty': 'beginner',
                'pronunciation_tips': 'nais-tu-MEET-yu',
                'common_mistakes': ['Forgetting to link "to" and "meet"']
            },
            {
                'text': 'Welcome',
                'translation': 'Bem-vindo(a)',
                'usage_example': 'Welcome to our home!',
                'difficulty': 'beginner',
                'pronunciation_tips': 'WEL-kum',
                'common_mistakes': ['Pronouncing the "l" too strongly']
            },
            {
                'text': 'Yo',
                'translation': 'Ei (informal)',
                'usage_example': "Yo! What's new?",
                'difficulty': 'intermediate',
                'pronunciation_tips': 'yoh',
                'common_mistakes': ['Using it in formal situations']
            },
            {
                'text': 'Howdy',
                'translation': 'Olá (informal)',
                'usage_example': 'Howdy! How are you doing?',
                'difficulty': 'intermediate',
                'pronunciation_tips': 'HOW-dee',
                'common_mistakes': ['Using it outside casual contexts']
            },
            {
                'text': 'Greetings',
                'translation': 'Saudações',
                'usage_example': 'Greetings, everyone!',
                'difficulty': 'intermediate',
                'pronunciation_tips': 'GREE-tings',
                'common_mistakes': ['Making it sound too formal']
            },
            {
                'text': 'Hi there',
                'translation': 'Olá (amigável)',
                'usage_example': 'Hi there! Can I help you?',
                'difficulty': 'beginner',
                'pronunciation_tips': 'hai-THERE',
                'common_mistakes': ['Not emphasizing "there"']
            },
            {
                'text': 'Good day',
                'translation': 'Bom dia (formal)',
                'usage_example': 'Good day, sir!',
                'difficulty': 'intermediate',
                'pronunciation_tips': 'gud-DAY',
                'common_mistakes': ['Using it too casually']
            },
            {
                'text': 'How do you do',
                'translation': 'Como vai (muito formal)',
                'usage_example': 'How do you do, Mr. Smith?',
                'difficulty': 'advanced',
                'pronunciation_tips': 'how-do-you-DOO',
                'common_mistakes': ['Using it as a question']
            },
            {
                'text': 'Hey there',
                'translation': 'Oi (casual)',
                'usage_example': 'Hey there! Long time no see!',
                'difficulty': 'beginner',
                'pronunciation_tips': 'hey-THERE',
                'common_mistakes': ['Making it sound too formal']
            },
            {
                'text': 'Morning',
                'translation': 'Bom dia (informal)',
                'usage_example': "Morning! Beautiful day, isn't it?",
                'difficulty': 'beginner',
                'pronunciation_tips': 'MOR-ning',
                'common_mistakes': ['Using it in formal situations']
            },
            {
                'text': 'Evening',
                'translation': 'Boa noite (informal)',
                'usage_example': 'Evening! Nice party!',
                'difficulty': 'beginner',
                'pronunciation_tips': 'EE-vning',
                'common_mistakes': ['Using it formally without "good"']
            }
        ]

    def get_all_greetings(self):
        return self.greetings

    def get_greeting_by_text(self, text):
        return next((g for g in self.greetings if g['text'].lower() == text.lower()), None)

    def get_greetings_by_difficulty(self, difficulty):
        return [g for g in self.greetings if g['difficulty'] == difficulty]

    def check_pronunciation(self, text, user_pronunciation):
        greeting = self.get_greeting_by_text(text)
        if not greeting:
            return {'error': 'Greeting not found'}

        # Aqui você pode implementar a lógica real de verificação de pronúncia
        # Por enquanto, retornamos apenas as dicas e erros comuns
        return {
            'tips': greeting['pronunciation_tips'],
            'common_mistakes': greeting['common_mistakes']
        }