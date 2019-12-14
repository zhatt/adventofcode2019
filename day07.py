#!/usr/bin/env python3

from itertools import permutations

import aoc
import int_code_computer


def parse_input(line):
    int_code = list(map(int, line.split(',')))
    return int_code


def get_phases_permutations(feedback_mode):
    if feedback_mode:
        # Permute 5 - 9.
        generator =  permutations(range(5, 10))
    else:
        # Permute 0 - 4.
        generator = permutations(range(0, 5))
    return generator


def simulate_amplifiers(int_code, feedback_mode):
    # pylint: disable=too-many-locals
    max_output = 0

    for phase_configuration in get_phases_permutations(feedback_mode):
        # First computer gets 0 for input.
        stream_into_a = [phase_configuration[0], 0]
        stream_into_b = [phase_configuration[1]]
        stream_into_c = [phase_configuration[2]]
        stream_into_d = [phase_configuration[3]]
        stream_into_e = [phase_configuration[4]]

        amp_a = int_code_computer.IntCodeComputer(int_code, stream_into_a, stream_into_b)
        amp_b = int_code_computer.IntCodeComputer(int_code, stream_into_b, stream_into_c)
        amp_c = int_code_computer.IntCodeComputer(int_code, stream_into_c, stream_into_d)
        amp_d = int_code_computer.IntCodeComputer(int_code, stream_into_d, stream_into_e)
        amp_e = int_code_computer.IntCodeComputer(int_code, stream_into_e, stream_into_a)

        if feedback_mode:
            until = int_code_computer.IntCodeComputer.OUTPUT
        else:
            until = int_code_computer.IntCodeComputer.HALT

        while not amp_e.is_halted():
            amp_a.run(until=until)
            amp_b.run(until=until)
            amp_c.run(until=until)
            amp_d.run(until=until)
            amp_e.run(until=until)

        last_output = stream_into_a[0]
        if last_output > max_output:
            max_output = last_output

    return max_output


def part1(input_list):
    int_code = parse_input(input_list[0])
    return simulate_amplifiers(int_code, feedback_mode=False)


def part2(input_list):
    int_code = parse_input(input_list[0])
    return simulate_amplifiers(int_code, feedback_mode=True)


if __name__ == "__main__":
    aoc.main(part1, part2)
