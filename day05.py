#!/usr/bin/env python3

import aoc
import int_code_computer


def parse_input(line):
    int_code = list(map(int, line.split(',')))
    return int_code


def part1(input_list):
    """
    Basic test of int code computer.  Run air conditioning diagnostic.
    """

    int_code = parse_input(input_list[0])

    input_stream = [1]  # System ID for air conditioning.
    output_stream = []
    computer = int_code_computer.IntCodeComputer(int_code, input_stream, output_stream)
    computer.run()
    return output_stream[-1]


def part2(input_list):
    """
    Run thermal radiator controller diagnostic.
    """

    int_code = parse_input(input_list[0])

    input_stream = [5]  # System ID for thermal radiator controller.
    output_stream = []
    computer = int_code_computer.IntCodeComputer(int_code, input_stream, output_stream)
    computer.run()
    return output_stream[-1]


if __name__ == "__main__":
    aoc.main(part1, part2)
