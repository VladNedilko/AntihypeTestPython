import unittest
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class MockCharacter:
    def __init__(self, name):
        self.name = name

class TestGameCharacters(unittest.TestCase):
    def setUp(self):
        self.e = MockCharacter("Монолог героя")
        self.a = MockCharacter("Кіт")
        self.r = MockCharacter("Раян Гослінг")
        self.audio_mus1 = "cloth-flapping-in-wind-74205.mp3"
        self.audio_mus2 = "6d64cbf7b17425e.mp3"

    def test_character_names(self):
        self.assertEqual(self.e.name, "Монолог героя")
        self.assertEqual(self.a.name, "Кіт")
        self.assertEqual(self.r.name, "Раян Гослінг")

    def test_audio_definitions(self):
        self.assertEqual(self.audio_mus1, "cloth-flapping-in-wind-74205.mp3")
        self.assertEqual(self.audio_mus2, "6d64cbf7b17425e.mp3")

if __name__ == '__main__':
    unittest.main()