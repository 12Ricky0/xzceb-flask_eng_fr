import unittest
from translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase):

    def test1(self):
        self.assertEquals(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('hello'), 'bonjour')


class testFrenchToEnglish(unittest.TestCase):

    def test1(self):
        self.assertEquals(french_to_english('Bonjour'), 'Hello')
        self.assertEquals(french_to_english('bonjour'), 'hello')

unittest.main()