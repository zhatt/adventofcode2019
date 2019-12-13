import unittest

import aoc
import day06


class TestDay06(unittest.TestCase):

    def test_part1_example(self):
        input_list = [
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
        ]

        result = day06.part1(input_list)
        self.assertEqual(42, result)

    def test_part1_input(self):
        result = day06.part1(aoc.read_input('day06.input'))
        self.assertEqual(273985, result)


    def test_part2_example(self):
        input_list = [
            "COM)B",
            "B)C",
            "C)D",
            "D)E",
            "E)F",
            "B)G",
            "G)H",
            "D)I",
            "E)J",
            "J)K",
            "K)L",
            "K)YOU",
            "I)SAN",
        ]

        result = day06.part2(input_list)
        self.assertEqual(4, result)

    def test_part2_input(self):
        result = day06.part2(aoc.read_input('day06.input'))
        self.assertEqual(460, result)

if __name__ == '__main__':
    unittest.main()
