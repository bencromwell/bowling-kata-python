import unittest
from bowling.game import Game


class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def roll_many(self, num_rolls, pins):
        for i in range(0, num_rolls):
            self.g.roll(pins)

    def test_gutter_game(self):
        self.roll_many(num_rolls=20, pins=0)
        self.assertEqual(0, self.g.score)

    def test_all_ones(self):
        self.roll_many(num_rolls=20, pins=1)
        self.assertEqual(20, self.g.score)

    def test_one_spare(self):
        self.roll_spare()
        self.g.roll(3)
        self.roll_many(num_rolls=17, pins=0)
        self.assertEqual(16, self.g.score)

    def test_one_strike(self):
        self.roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(24, self.g.score)

    def test_perfect_game(self):
        self.roll_many(12, 10)
        self.assertEqual(300, self.g.score)

    def roll_strike(self):
        self.g.roll(10)

    def roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)


if __name__ == '__main__':
    unittest.main()
