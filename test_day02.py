import unittest

import aoc
import day02
import int_code_computer


class TestDay01(unittest.TestCase):

    def test_parse_input(self):
        int_code = day02.parse_input("1,0,0,0,99")
        self.assertEqual([1, 0, 0, 0, 99], int_code)

    def test_part1_example1(self):
        int_code = [1, 0, 0, 0, 99]
        computer = int_code_computer.IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([2, 0, 0, 0, 99], memory)

    def test_part1_example2(self):
        int_code = [2, 3, 0, 3, 99]
        computer = int_code_computer.IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([2, 3, 0, 6, 99], memory)

    def test_part1_example3(self):
        int_code = [2, 4, 4, 5, 99, 0]
        computer = int_code_computer.IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([2, 4, 4, 5, 99, 9801], memory)

    def test_part1_example4(self):
        int_code = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        computer = int_code_computer.IntCodeComputer(int_code)
        computer.run()
        memory = computer.dump()
        self.assertEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], memory)

    def test_part1_input(self):
        result = day02.part1(aoc.read_input('day02.input'))
        self.assertEqual(9706670, result)

    def test_part2_input(self):
        result = day02.part2(aoc.read_input('day02.input'))
        self.assertEqual(result, 2552)


if __name__ == '__main__':
    unittest.main()
