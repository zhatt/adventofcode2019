import unittest

import aoc
import day02


class TestDay02(unittest.TestCase):

    def test_part1_input(self):
        result = day02.part1(aoc.read_input('day02.input'))
        self.assertEqual(9706670, result)

    def test_part2_input(self):
        result = day02.part2(aoc.read_input('day02.input'))
        self.assertEqual(result, 2552)


if __name__ == '__main__':
    unittest.main()
