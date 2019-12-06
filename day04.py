#!/usr/bin/env python3

import aoc


# The default algorithm is supposed to check triples but part one skips that.
def is_valid_password(number, exclude_triples=False):
    found_pair = False
    is_increasing = True

    # Add end of list sentinels.  These are correct for sequencing increase but won't form a
    # double or triple. We wil insert the rest of the numbers to test between -1 and 10.
    digits = [-1, 10, 11]

    while number > 0:
        digits.insert(1, number % 10)
        number //= 10

    for index, _ in enumerate(digits):
        if index < 1 or index > len(digits) - 3:
            # Skip sentinels.
            continue

        # Find doubles.
        if digits[index] == digits[index + 1]:
            if not exclude_triples:
                if digits[index - 1] != digits[index] and digits[index + 2] != digits[index]:
                    found_pair = True
            else:
                found_pair = True

        # Must not decrease values.
        if digits[index] > digits[index + 1]:
            is_increasing = False

    return found_pair and is_increasing


def part1(input_list):
    start, end = map(int, input_list[0].split('-'))

    number_of_valid_passwords = 0

    for password in range(start, end + 1):
        if is_valid_password(password, exclude_triples=True):
            number_of_valid_passwords += 1

    return number_of_valid_passwords


def part2(input_list):
    start, end = map(int, input_list[0].split('-'))

    number_of_valid_passwords = 0

    for password in range(start, end + 1):
        if is_valid_password(password):
            number_of_valid_passwords += 1

    return number_of_valid_passwords


if __name__ == "__main__":
    aoc.main(part1, part2)
