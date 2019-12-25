import unittest

import aoc
import day13


class TestDay13(unittest.TestCase):

    def test_part1_input(self):
        result = day13.part1(aoc.read_input('day13.input'))
        self.assertEqual(376, result)

    def test_part2_input(self):
        result = day13.part2(aoc.read_input('day13.input'))
        self.assertEqual(18509, result)


if __name__ == '__main__':
    unittest.main()
