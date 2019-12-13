import unittest

import aoc
import day05


class TestDay05(unittest.TestCase):

    def test_part1_input(self):
        result = day05.part1(aoc.read_input('day05.input'))
        self.assertEqual(4887191, result)

    def test_part2_input(self):
        result = day05.part2(aoc.read_input('day05.input'))
        self.assertEqual(3419022, result)


if __name__ == '__main__':
    unittest.main()
