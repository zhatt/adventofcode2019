import unittest

import aoc
import day15


class TestDay13(unittest.TestCase):

    def test_part1_input(self):
        result = day15.part1(aoc.read_input('day15.input'))
        self.assertEqual(220, result)

    def test_part2_input(self):
        result = day15.part2(aoc.read_input('day15.input'))
        self.assertEqual(334, result)


if __name__ == '__main__':
    unittest.main()
