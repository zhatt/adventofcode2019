import unittest

import aoc
import day09


class TestDay09(unittest.TestCase):

    def test_part1_input(self):
        result = day09.part1(aoc.read_input('day09.input'))
        self.assertEqual(3742852857, result)

    def test_part2_input(self):
        result = day09.part2(aoc.read_input('day09.input'))
        self.assertEqual(73439, result)


if __name__ == '__main__':
    unittest.main()
