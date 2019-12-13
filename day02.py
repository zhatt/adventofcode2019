#!/usr/bin/env python3
import itertools

import aoc
import int_code_computer


def part1(input_list):
    """
    Basic test of int code computer.
    """

    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    int_code[1] = 12
    int_code[2] = 2

    computer = int_code_computer.IntCodeComputer(int_code)
    computer.run()
    return computer.get_memory(0)


def part2(input_list):
    """
    Find int code noun and verb that produces the desired output.
    """

    desired_output = 19690720

    noun = None  #for PyLint
    verb = None  #for PyLint
    for noun, verb in itertools.product(range(100), range(100)):
        int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

        int_code[1] = noun
        int_code[2] = verb

        computer = int_code_computer.IntCodeComputer(int_code)
        computer.run()
        result = computer.get_memory(0)
        if result == desired_output:
            break

    return noun * 100 + verb


if __name__ == "__main__":
    aoc.main(part1, part2)
