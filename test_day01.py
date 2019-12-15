import unittest

import aoc
import day01


class TestDay01(unittest.TestCase):

    def test_part1_example1(self):
        result = day01.part1((12,))
        self.assertEqual(result, 2)

    def test_part1_example2(self):
        result = day01.part1((14,))
        self.assertEqual(result, 2)

    def test_part1_example3(self):
        result = day01.part1((1969,))
        self.assertEqual(result, 654)

    def test_part1_example4(self):
        result = day01.part1((100756,))
        self.assertEqual(result, 33583)

    def test_part1_total(self):
        result = day01.part1((12, 14))
        self.assertEqual(result, 4)

    def test_part1_input(self):
        result = day01.part1(aoc.read_input('day01.input'))
        self.assertEqual(result, 3406432)

    def test_part2_example1(self):
        result = day01.part2((14,))
        self.assertEqual(result, 2)

    def test_part2_example2(self):
        result = day01.part2((1969,))
        self.assertEqual(result, 966)

    def test_part2_example3(self):
        result = day01.part2((100756,))
        self.assertEqual(result, 50346)

    def test_part2_input(self):
        result = day01.part2(aoc.read_input('day01.input'))
        self.assertEqual(result, 5106777)


if __name__ == '__main__':
    unittest.main()
