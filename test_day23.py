import unittest

import aoc
import day23

from int_code_computer import IntCodeComputer

ICC = IntCodeComputer


class TestDay23(unittest.TestCase):

    def test_input_generator(self):
        # Test that the NetworkComputer automatically generates -1 for input if there is no input
        int_code = [
            ICC.INPUT + ICC.MODE1_POS, 100,  # Write input to 100
            ICC.OUTPUT + ICC.MODE1_POS, 100,  # Output from 100
            ICC.JMP_IF_TRUE + ICC.MODE1_IMM + ICC.MODE2_IMM, 1, 0,
        ]

        computer = day23.NetworkComputer(int_code, 0)

        computer.step()
        computer.step()
        computer.step()
        output = computer.output_stream
        self.assertEqual([0], output)

        computer.step()
        computer.step()
        computer.step()
        output = computer.output_stream
        self.assertEqual([0, -1], output)

        computer.input_stream.append(10)
        computer.step()
        computer.step()
        computer.step()
        computer.step()
        computer.step()
        computer.step()
        output = computer.output_stream
        self.assertEqual([0, -1, 10, -1], output)

    def test_part1_input(self):
        result = day23.part1(aoc.read_input('day23.input'))
        self.assertEqual(21089, result)

    def test_part2_input(self):
        result = day23.part2(aoc.read_input('day23.input'))
        self.assertEqual(16658, result)


if __name__ == '__main__':
    unittest.main()
