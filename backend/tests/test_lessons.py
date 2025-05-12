import unittest
from vocabulary.greetings import Greetings
from vocabulary.lessons import GreetingLessons
from vocabulary.contexts import get_vocabulary_by_context, get_all_contexts, get_word_details

class TestGreetingLessons(unittest.TestCase):
    def setUp(self):
        self.greetings = Greetings()
        self.lessons = GreetingLessons(self.greetings)

    def test_get_lesson_by_level(self):
        lesson = self.lessons.get_lesson_by_level(1)
        self.assertIsNotNone(lesson)
        self.assertEqual(lesson['level'], 1)
        self.assertEqual(lesson['title'], 'Saudações Básicas')

        # Teste com nível inexistente
        lesson = self.lessons.get_lesson_by_level(99)
        self.assertIsNone(lesson)

    def test_get_all_lessons(self):
        lessons = self.lessons.get_all_lessons()
        self.assertIsInstance(lessons, list)
        self.assertEqual(len(lessons), 3)  # Verificando se temos 3 níveis de lições
        self.assertEqual(lessons[0]['level'], 1)
        self.assertEqual(lessons[1]['level'], 2)
        self.assertEqual(lessons[2]['level'], 3)

    def test_get_lesson_greetings(self):
        greetings = self.lessons.get_lesson_greetings(1)
        self.assertIsInstance(greetings, list)
        self.assertTrue(len(greetings) > 0)
        # Verificando se todas as saudações são do nível 1
        lesson = self.lessons.get_lesson_by_level(1)
        for greeting in greetings:
            self.assertIn(greeting['text'], lesson['greetings'])

        # Teste com nível inexistente
        greetings = self.lessons.get_lesson_greetings(99)
        self.assertEqual(len(greetings), 0)

    def test_check_lesson_progress(self):
        # Teste com exercícios completos
        progress = self.lessons.check_lesson_progress(1, ['pronunciation', 'translation'])
        self.assertEqual(progress['level'], 1)
        self.assertEqual(progress['progress_percentage'], 100)
        self.assertTrue(progress['completed'])

        # Teste com exercícios parcialmente completos
        progress = self.lessons.check_lesson_progress(1, ['pronunciation'])
        self.assertEqual(progress['progress_percentage'], 66.66666666666667)  # 10 de 15 pontos
        self.assertFalse(progress['completed'])

        # Teste com nível inexistente
        progress = self.lessons.check_lesson_progress(99, [])
        self.assertIn('error', progress)

if __name__ == '__main__':
    unittest.main()