import unittest

import aoc
import day19


class TestDay19(unittest.TestCase):

    def test_part1_input(self):
        result = day19.part1(aoc.read_input('day19.input'))
        self.assertEqual(162, result)

    def test_part2_input(self):
        result = day19.part2(aoc.read_input('day19.input'))
        self.assertEqual(13021056, result)


if __name__ == '__main__':
    unittest.main()
