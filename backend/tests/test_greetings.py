import unittest
from vocabulary.greetings import Greetings

class TestGreetings(unittest.TestCase):
    def setUp(self):
        self.greetings = Greetings()

    def test_get_all_greetings(self):
        greetings = self.greetings.get_all_greetings()
        self.assertIsInstance(greetings, list)
        self.assertTrue(len(greetings) > 0)
        self.assertIn('text', greetings[0])
        self.assertIn('translation', greetings[0])

    def test_get_greeting_by_text(self):
        greeting = self.greetings.get_greeting_by_text('Hello')
        self.assertIsNotNone(greeting)
        self.assertEqual(greeting['text'], 'Hello')
        self.assertEqual(greeting['translation'], 'Olá')

        # Teste com texto inexistente
        greeting = self.greetings.get_greeting_by_text('NonExistent')
        self.assertIsNone(greeting)

    def test_get_greetings_by_difficulty(self):
        beginner_greetings = self.greetings.get_greetings_by_difficulty('beginner')
        self.assertTrue(len(beginner_greetings) > 0)
        for greeting in beginner_greetings:
            self.assertEqual(greeting['difficulty'], 'beginner')

    def test_check_pronunciation(self):
        result = self.greetings.check_pronunciation('Hello', 'hello')
        self.assertIn('tips', result)
        self.assertIn('common_mistakes', result)

        # Teste com saudação inexistente
        result = self.greetings.check_pronunciation('NonExistent', 'test')
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()