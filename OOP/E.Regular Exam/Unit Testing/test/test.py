from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Dimitar", 19, 7)

    def test_successful_initialization(self):
        self.assertEqual("Dimitar", self.tennis_player.name)
        self.assertEqual(19, self.tennis_player.age)
        self.assertEqual(7, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer("g", 20, 8)

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer("gg", 20, 8)

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_invalid_age(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player = TennisPlayer("George", 4, 17)

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_unsuccessful_add_new_win(self):
        self.tennis_player.wins = ["Le copa Italia"]
        result = self.tennis_player.add_new_win("Le copa Italia")
        self.assertEqual(f"Le copa Italia has been already added to the list of wins!", result)

    def test_successful_add_new_win(self):
        self.tennis_player.add_new_win("Golden Years")
        self.assertEqual("Golden Years", self.tennis_player.wins[0])

    def test_less_than_False(self):
        second_player = TennisPlayer("Gorge", 21, 4)
        result = self.tennis_player < second_player
        self.assertEqual(f'Dimitar is a better player than Gorge', result)

    def test_less_than_True(self):
        second_player = TennisPlayer("Gorge", 21, 17)
        result = self.tennis_player < second_player
        self.assertEqual(f'Gorge is a top seeded player and he/she is better than Dimitar', result)

    def test_string_return(self):
        self.tennis_player.wins = ["Le copa Italia", "Golden Years 2nd edition"]
        result = f"Tennis Player: Dimitar\n" \
                 f"Age: 19\n" \
                 f"Points: 7.0\n" \
                 f"Tournaments won: Le copa Italia, Golden Years 2nd edition"
        self.assertEqual(result, str(self.tennis_player))


if __name__ == '__main__':
    main()
