# Módulo de lições para saudações

class GreetingLessons:
    def __init__(self, greetings):
        self.greetings = greetings
        self.lessons = [
            {
                'level': 1,
                'title': 'Saudações Básicas',
                'description': 'Aprenda as saudações mais comuns do dia a dia',
                'greetings': ['Hello', 'Hi', 'Good morning', 'Good afternoon', 'Good evening', 'Good night'],
                'exercises': [
                    {
                        'type': 'pronunciation',
                        'instructions': 'Pratique a pronúncia das saudações básicas',
                        'points': 10
                    },
                    {
                        'type': 'translation',
                        'instructions': 'Traduza as saudações para português',
                        'points': 5
                    }
                ]
            },
            {
                'level': 2,
                'title': 'Saudações Informais',
                'description': 'Aprenda saudações casuais para conversas informais',
                'greetings': ['Hey', "What's up", 'Hi there', 'Hey there', 'Morning', 'Evening'],
                'exercises': [
                    {
                        'type': 'context',
                        'instructions': 'Identifique situações apropriadas para cada saudação',
                        'points': 15
                    },
                    {
                        'type': 'pronunciation',
                        'instructions': 'Pratique a pronúncia informal',
                        'points': 10
                    }
                ]
            },
            {
                'level': 3,
                'title': 'Saudações Formais e Expressões',
                'description': 'Aprenda saudações formais e expressões de cumprimento',
                'greetings': ['How do you do', 'Good day', 'Greetings', 'Welcome', 'Nice to meet you'],
                'exercises': [
                    {
                        'type': 'formal_context',
                        'instructions': 'Pratique o uso de saudações em ambientes formais',
                        'points': 20
                    },
                    {
                        'type': 'pronunciation',
                        'instructions': 'Foque na pronúncia clara e formal',
                        'points': 15
                    }
                ]
            }
        ]

    def get_lesson_by_level(self, level):
        """Retorna uma lição específica pelo nível"""
        return next((lesson for lesson in self.lessons if lesson['level'] == level), None)

    def get_all_lessons(self):
        """Retorna todas as lições disponíveis"""
        return self.lessons

    def get_lesson_greetings(self, level):
        """Retorna todas as saudações de uma lição específica"""
        lesson = self.get_lesson_by_level(level)
        if not lesson:
            return []
        return [g for g in self.greetings.get_all_greetings() if g['text'] in lesson['greetings']]

    def check_lesson_progress(self, level, completed_exercises):
        """Calcula o progresso e pontuação em uma lição"""
        lesson = self.get_lesson_by_level(level)
        if not lesson:
            return {'error': 'Lição não encontrada'}

        total_points = sum(ex['points'] for ex in lesson['exercises'])
        earned_points = sum(ex['points'] for ex in lesson['exercises'] 
                          if ex['type'] in completed_exercises)

        return {
            'level': level,
            'total_points': total_points,
            'earned_points': earned_points,
            'progress_percentage': (earned_points / total_points) * 100 if total_points > 0 else 0,
            'completed': earned_points == total_points
        }