#!/usr/bin/env python3
import itertools

import aoc


def generate_pattern(position):
    # phase starts at 1 to match examples.
    # Adjust phase to 0 based.
    base_pattern = (0, 1, 0, -1)

    # gen1 generates the base pattern with each digit repeated position times.
    def gen1(position):
        for value in base_pattern:
            for value_rep in itertools.repeat(value, position):
                yield value_rep

    # gen2 cycles the gen1 pattern
    def gen2(position):
        # phase starts at 1 to match examples.
        # Adjust phase to 0 based.

        for value in itertools.cycle(gen1(position)):
            yield value

    # Skip the first value in the gen2 sequence to produce the desired pattern.
    for value in itertools.islice(gen2(position), 1, None):
        yield value


def do_phase(input_signal, iterations=1):
    output_signal_list = list(map(int, input_signal))

    for _ in range(iterations):
        input_signal_list = output_signal_list.copy()
        output_signal_list = []
        for position in range(1, len(input_signal_list) + 1):
            signal_sum = 0
            for val1, val2 in zip(input_signal_list, generate_pattern(position)):
                signal_sum += val1 * val2

            signal_sum = abs(signal_sum) % 10
            output_signal_list.append(signal_sum)

    output_signal = "".join(map(str, output_signal_list))
    return output_signal


def part1(input_list):
    input_signal = input_list[0]
    output_signal = do_phase(input_signal, 100)
    return output_signal[0:8]


def validate_pattern_assumption(total_length, offset):
    # We assume that we are looking for a message towards the end of the signal data.  We also
    # assume that the pattern will all be ones from there to the end.  This makes calculating the
    # 100th phase faster.  It appears that all given inputs meet these requirements.
    pattern_sum = sum(itertools.islice(generate_pattern(offset), offset, total_length))
    assert pattern_sum == total_length - offset


def part2(input_list):
    input_signal = input_list[0]
    signal_offset = int(input_signal[:7])
    total_length = len(input_signal) * 10000

    # Validate that the pattern is all ones in from our signal to the end.
    validate_pattern_assumption(total_length, signal_offset)

    # We will calculate the signal from signal_offset to end.  Since the pattern is all ones in that
    # region each value is the sum of the values from that position to the end modulus 10.
    #
    # We will actually do the calculation on the reversed data because it is easier to make the
    # Python list and iterator functions work.

    length_from_signal_offset_to_end = total_length - signal_offset
    reversed_digits = list(map(int, itertools.islice(itertools.cycle(reversed(input_signal)),
                                                     length_from_signal_offset_to_end)))
    for _ in range(100):
        # Accumulate values from this location to the front of the list (note this is really from
        # this location to the end of the list since the list is reversed).  Then take only the
        # ones location.
        reversed_digits = list(itertools.accumulate(reversed_digits))
        for index, _ in enumerate(reversed_digits):
            reversed_digits[index] %= 10

    # The signal is the last eight values.  Reverse them to undo the above reverse.
    output_signal = "".join(map(str, reversed(reversed_digits[-8:])))

    return output_signal


if __name__ == "__main__":
    aoc.main(part1, part2)
