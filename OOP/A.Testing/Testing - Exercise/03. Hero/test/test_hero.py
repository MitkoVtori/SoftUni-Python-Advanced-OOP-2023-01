from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Superman", 7, 100, 15)

    def test_successful_initialization(self):
        self.assertEqual("Superman", self.hero.username)
        self.assertEqual(7, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle_fighting_yourself_raises_exception(self):
        enemy = Hero("Superman", 7, 100, 15)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_health_raises_value_error(self):
        enemy = Hero("Batman", 19, 180, 65)
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_less_than_zero_health_raises_value_error(self):
        enemy = Hero("Batman", 19, 180, 65)
        self.hero.health = -1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_with_enemy_zero_health_raises_value_error(self):
        enemy = Hero("Batman", 19, 0, 65)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight Batman. He needs to rest", str(ve.exception))

    def test_battle_with_less_than_zero_enemy_health_raises_value_error(self):
        enemy = Hero("Batman", 19, -1, 65)

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight Batman. He needs to rest", str(ve.exception))

    def test_battle_draw(self):
        enemy = Hero("Batman", 7, 100, 15)
        result = self.hero.battle(enemy)
        health = 100 - (7 * 15)
        self.assertEqual(health, self.hero.health)
        self.assertEqual(health, enemy.health)
        self.assertEqual("Draw", result)

    def test_hero_wins(self):
        enemy = Hero("Batman", 2, 1, 1)

        result = self.hero.battle(enemy)
        enemy_health = 1 - (7 * 15)
        hero_level = 7 + 1
        hero_health = (100 - 2) + 5
        hero_damage = 15 + 5

        self.assertEqual(enemy_health, enemy.health)
        self.assertEqual(hero_level, self.hero.level)
        self.assertEqual(hero_health, self.hero.health)
        self.assertEqual(hero_damage, self.hero.damage)
        self.assertEqual("You win", result)

    def test_enemy_wins(self):
        enemy = Hero("Batman", 7, 100, 15)
        self.hero = Hero("Superman", 2, 1, 1)

        result = self.hero.battle(enemy)
        hero_health = 1 - (7 * 15)
        enemy_level = 7 + 1
        enemy_health = (100 - 2) + 5
        enemy_damage = 15 + 5

        self.assertEqual(hero_health, self.hero.health)
        self.assertEqual(enemy_level, enemy.level)
        self.assertEqual(enemy_health, enemy.health)
        self.assertEqual(enemy_damage, enemy.damage)
        self.assertEqual("You lose", result)

    def test_str_method_successful_string_return(self):
        result = f"Hero Superman: 7 lvl\n" \
                 f"Health: 100\n" \
                 f"Damage: 15\n"

        self.assertEqual(result, str(self.hero))


if __name__ == '__main__':
    main()
