#!/usr/bin/env python3

import aoc
import int_code_computer


# SpringDroid jumps 4.
#
# These are the patterns I found.
# #####...#########   NOT 1 and 4
# #####..#.########   NOT 2 and 4
# #####.#..########   NOT 3 and 4
# #####.#.##.######   :3 is jumping too early need to block if if NOT 8
#
# My code.
# NOT A T  pattern 1
# AND D T
# OR T J
#
# NOT B T  pattern 2
# AND D T
# OR T J
#
# NOT C T  pattern 3
# AND D T
# AND H T  added for pattern 4
# OR T J
#


class SpringDroid:
    # pylint: disable=too-few-public-methods

    def __init__(self, int_code):
        self._int_code = int_code.copy()

    def run(self, ascii_code):
        input_stream = list(map(ord, ascii_code))
        output_stream = []
        computer = int_code_computer.IntCodeComputer(self._int_code, input_stream, output_stream)
        computer.run()

        if output_stream[-1] < 256:
            camera_output = "".join(map(chr, output_stream))
            damage = None
        else:
            camera_output = None
            damage = output_stream[-1]

        return camera_output, damage


def part1(input_list):
    ascii_code = \
        "NOT A T\n" \
        "AND D T\n" \
        "OR T J\n" \
        "" \
        "NOT B T\n" \
        "AND D T\n" \
        "OR T J\n" \
        "" \
        "NOT C T\n" \
        "AND D T\n" \
        "OR T J\n" \
        "" \
        "WALK\n"

    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])
    springdroid = SpringDroid(int_code)

    camera_output, damage = springdroid.run(ascii_code)
    if camera_output:
        print(camera_output)
    return damage


def part2(input_list):
    ascii_code = \
        "NOT A T\n" \
        "AND D T\n" \
        "OR T J\n" \
        "" \
        "NOT B T\n" \
        "AND D T\n" \
        "OR T J\n" \
        "" \
        "NOT C T\n" \
        "AND D T\n" \
        "AND H T\n" \
        "OR T J\n" \
        "" \
        "RUN\n"

    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])
    springdroid = SpringDroid(int_code)

    camera_output, damage = springdroid.run(ascii_code)
    if camera_output:
        print(camera_output)
    return damage


if __name__ == "__main__":
    aoc.main(part1, part2)
