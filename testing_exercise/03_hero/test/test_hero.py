from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.oto = Hero('Oto', 10, 50.5, 2.5)
        self.enemy = Hero('Hero', 20, 0, 1)

    def test_correct_input(self):
        self.assertEqual('Oto', self.oto.username)
        self.assertEqual(10, self.oto.level)
        self.assertEqual(50.5, self.oto.health)
        self.assertEqual(2.5, self.oto.damage)

    def test_correct_str_output_data(self):
        expected_result = f"Hero {self.oto.username}: {self.oto.level} lvl\n" \
               f"Health: {self.oto.health}\n" \
               f"Damage: {self.oto.damage}\n"

        self.assertEqual(expected_result, self.oto.__str__())

    def test_battle_with_same_enemy_username_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.oto.battle(Hero('Oto', 20, 5.5, 1))

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_health_below_zero_when_battle_raise_value_error(self):
        self.oto.health = 0
        with self.assertRaises(ValueError) as ve:
            self.oto.battle(Hero('Enemy', 20, 5.5, 1))

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_if_enemy_health_below_zero_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.oto.battle(self.enemy)

        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_if_both_heroes_have_negative_health_after_battle_returns_draw(self):
        self.Draw = Hero('Draw', 20, 20, 5)
        oto_damage = self.oto.level * self.oto.damage    #25, same for enemy damage
        self.oto.health = 100 - self.oto.health
        result = self.oto.battle(self.Draw)
        self.Draw.health = -5

        self.assertEqual("Draw", result)

    def test_if_enemy_has_health_below_zero_returns_you_win(self):
        self.loser = Hero('Loser', 5, 1, 1)
        result = self.oto.battle(self.loser)

        self.assertEqual("You win", result)
        self.assertEqual(11, self.oto.level)
        self.assertEqual(50.5, self.oto.health)
        self.assertEqual(7.5, self.oto.damage)

    def test_when_enemy_stronger_hero_loses(self):
        self.winner = Hero('Winner', 20, 50, 10)
        result = self.oto.battle(self.winner)

        self.assertEqual("You lose", result)
        self.assertEqual(21, self.winner.level)
        self.assertEqual(30.0, self.winner.health)
        self.assertEqual(15, self.winner.damage)


if __name__ == '__main__':
    main()
