import unittest

import aoc
import day03


class TestDay03(unittest.TestCase):

    def test_part1_example1(self):
        input_list = [
            "R8,U5,L5,D3",
            "U7,R6,D4,L4"
        ]
        result = day03.part1(input_list)
        self.assertEqual(6, result)

    def test_part1_example2(self):
        input_list = [
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83"
        ]
        result = day03.part1(input_list)
        self.assertEqual(159, result)

    def test_part1_example3(self):
        input_list = [
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        ]
        result = day03.part1(input_list)
        self.assertEqual(135, result)

    def test_part1_input(self):
        result = day03.part1(aoc.read_input('day03.input'))
        self.assertEqual(293, result)

    def test_part2_example1(self):
        input_list = [
            "R8,U5,L5,D3",
            "U7,R6,D4,L4"
        ]
        result = day03.part2(input_list)
        self.assertEqual(30, result)

    def test_part2_example2(self):
        input_list = [
            "R75,D30,R83,U83,L12,D49,R71,U7,L72",
            "U62,R66,U55,R34,D71,R55,D58,R83"
        ]
        result = day03.part2(input_list)
        self.assertEqual(610, result)

    def test_part2_example3(self):
        input_list = [
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        ]
        result = day03.part2(input_list)
        self.assertEqual(410, result)

    def test_part2_input(self):
        result = day03.part2(aoc.read_input('day03.input'))
        self.assertEqual(27306, result)


if __name__ == '__main__':
    unittest.main()
