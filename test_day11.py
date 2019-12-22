import unittest

import aoc
import day11


class TestDay11(unittest.TestCase):

    def test_turning(self):
        # pylint: disable=protected-access
        bot = day11.PaintingRobot([], None)
        self.assertEqual(aoc.Coord(0, 1), bot._direction)
        bot.turn_left_and_move()
        self.assertEqual(aoc.Coord(-1, 0), bot._direction)
        bot.turn_left_and_move()
        self.assertEqual(aoc.Coord(0, -1), bot._direction)
        bot.turn_left_and_move()
        self.assertEqual(aoc.Coord(1, 0), bot._direction)
        bot.turn_left_and_move()
        self.assertEqual(aoc.Coord(0, 1), bot._direction)

        bot.turn_right_and_move()
        self.assertEqual(aoc.Coord(1, 0), bot._direction)
        bot.turn_right_and_move()
        self.assertEqual(aoc.Coord(0, -1), bot._direction)
        bot.turn_right_and_move()
        self.assertEqual(aoc.Coord(-1, 0), bot._direction)
        bot.turn_right_and_move()
        self.assertEqual(aoc.Coord(0, 1), bot._direction)

    def test_part1_input(self):
        result = day11.part1(aoc.read_input('day11.input'))
        self.assertEqual(2252, result)

    def test_part2_input(self):
        result = day11.part2(aoc.read_input('day11.input'))

        # Our ship's identifier is AGALRGJE
        expected = \
            "  **   **   **  *    ***   **    ** ****   \n" \
            " *  * *  * *  * *    *  * *  *    * *      \n" \
            " *  * *    *  * *    *  * *       * ***    \n" \
            " **** * ** **** *    ***  * **    * *      \n" \
            " *  * *  * *  * *    * *  *  * *  * *      \n" \
            " *  *  *** *  * **** *  *  ***  **  ****   \n"

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
