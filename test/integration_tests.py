import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class RenPyMock:
    def __init__(self):
        self.current_label = None

    def jump(self, label):
        self.current_label = label
        return label

    def menu(self, options):

        return options[0]

class TestGameFlow(unittest.TestCase):
    def setUp(self):
        self.renpy = RenPyMock()

    def test_start_to_library(self):
        choice = self.renpy.menu(["Піти до бібліотеки", "Повернутись додому"])
        self.assertEqual(choice, "Піти до бібліотеки")
        
        next_label = self.renpy.jump("library_scene")
        self.assertEqual(next_label, "library_scene")

    def test_library_to_catalog(self):
        self.renpy.jump("library_scene")
        next_label = self.renpy.jump("catalog_scene")
        self.assertEqual(next_label, "catalog_scene")

    def test_bookshelf_choice(self):
        choice = self.renpy.menu(["Взяти книгу", "Ігнорувати"])
        self.assertEqual(choice, "Взяти книгу")

        next_label = self.renpy.jump("take_book")
        self.assertEqual(next_label, "take_book")

if __name__ == '__main__':
    unittest.main()