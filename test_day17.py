import unittest

import aoc
import day17


class TestDay17(unittest.TestCase):

    def test_part1_input(self):
        result = day17.part1(aoc.read_input('day17.input'))
        self.assertEqual(5680, result)

    def test_part2_input(self):
        result = day17.part2(aoc.read_input('day17.input'))
        self.assertEqual(895965, result)


if __name__ == '__main__':
    unittest.main()
