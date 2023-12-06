from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.cat = Mammal("Pipi", "cat", "Meow")

    def test_correct_init(self):
        self.assertEqual("Pipi", self.cat.name)
        self.assertEqual("cat", self.cat.type)
        self.assertEqual("Meow", self.cat.sound)
        self.assertEqual("animals", self.cat.get_kingdom())

    def test_make_sound_returns_str(self):
        self.assertEqual(f"{self.cat.name} makes {self.cat.sound}", self.cat.make_sound())

    def test_info_returns_str(self):
        self.assertEqual(f"{self.cat.name} is of type {self.cat.type}", self.cat.info())


if __name__ == '__main__':
    main()
