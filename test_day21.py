import unittest

import aoc
import day21


class TestDay21(unittest.TestCase):

    def test_part1_input(self):
        result = day21.part1(aoc.read_input('day21.input'))
        self.assertEqual(19358870, result)

    def test_part2_input(self):
        result = day21.part2(aoc.read_input('day21.input'))
        self.assertEqual(1143356492, result)


if __name__ == '__main__':
    unittest.main()
