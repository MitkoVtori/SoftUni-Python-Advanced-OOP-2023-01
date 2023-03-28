from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Rex", "Lion", "ROAR!!!")

    def test_successful_initialization(self):
        self.assertEqual("Rex", self.mammal.name)
        self.assertEqual("Lion", self.mammal.type)
        self.assertEqual("ROAR!!!", self.mammal.sound)

    def test_make_sound(self):
        self.assertEqual("Rex makes ROAR!!!", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Rex is of type Lion", self.mammal.info())


if __name__ == '__main__':
    main()
