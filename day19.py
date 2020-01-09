#!/usr/bin/env python3
from collections import deque

import aoc
import int_code_computer

VERBOSE = False


class Computer():
    # pylint: disable=too-few-public-methods
    def __init__(self, int_code):
        self.int_code = int_code.copy()

    def check_point(self, coord):
        """
        :param coord:  aoc.Coord to check.
        :return:  True if point is in tractor beam area.
        """
        input_stream = [coord.x_val, coord.y_val]
        output_stream = []
        computer = int_code_computer.IntCodeComputer(self.int_code, input_stream, output_stream)
        computer.run()

        return output_stream[0] == 1


def find_tip_of_tractor_beam(int_code):
    """
    :param int_code:
    :return:  aoc.Coord coordinate of tip of tractor region.
    """
    computer = Computer(int_code)

    # We probably shouldn't see this case.  My input doesn't hit this and I expect there is always
    # a gap between the origin and the tip but just in case.
    if computer.check_point(aoc.Coord(1, 1)) or \
            computer.check_point(aoc.Coord(0, 1)) or \
            computer.check_point(aoc.Coord(1, 0)):
        return aoc.Coord(0, 0)

    for y_val in range(1, 11):
        for x_val in range(1, 11):
            coord = aoc.Coord(x_val, y_val)
            if computer.check_point(coord):
                return coord

    # If we get here, we to rework the algorithm because the tip is not for 10 by 10 region.
    assert False
    return None


def find_left_edge_of_tractor_beam(int_code, coord):
    """
    Find the left edge of tractor beam.
    :param int_code:
    :param coord:
    :return:
    """
    computer = Computer(int_code)

    while not computer.check_point(coord):
        coord = coord._replace(x_val=coord.x_val + 1)

    return coord


def find_right_edge_of_tractor_beam(int_code, coord):
    computer = Computer(int_code)
    # coord must be in tractor beam region.
    assert computer.check_point(coord)

    while computer.check_point(coord):
        coord = coord._replace(x_val=coord.x_val + 1)

    # Loop goes one past adjust result back.
    return coord._replace(x_val=coord.x_val - 1)


def part1(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    computer = Computer(int_code)

    area = 0

    # Walk the area.  This could be optimized like part 2 but run time is okay and this makes
    # is easier to print the beam shape.
    for y_val in range(50):
        for x_val in range(50):
            in_beam = computer.check_point(aoc.Coord(x_val, y_val))

            if VERBOSE:
                if in_beam:
                    print("#", end='')
                else:
                    print(".", end='')

            if in_beam:
                area += 1
        if VERBOSE:
            print()

    return area


def part2(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    first_coord = find_tip_of_tractor_beam(int_code)
    last_coord = first_coord

    # We will store beginning and ending coordinates for that last 100 rows analyzed.
    line_info = deque((), 100)

    while True:
        # Move to next row
        first_coord = first_coord._replace(y_val=first_coord.y_val + 1)
        last_coord = last_coord._replace(y_val=last_coord.y_val + 1)

        # Search for beginning of beam on this row.
        first_coord = find_left_edge_of_tractor_beam(int_code, first_coord)

        # In some of the first rows, the overlap from the previous row might be zero so make
        # sure that last_coord is actually at a coordinate that is in the beam.  Otherwise,
        # find_last will assert.
        if last_coord.x_val < first_coord.x_val:
            last_coord = first_coord

        # Search for end of beam on this row.
        last_coord = find_right_edge_of_tractor_beam(int_code, last_coord)

        # Saving 100 info about 100 lines.
        line_info.append((first_coord, last_coord))

        # Once we have 100 lines, we can start checking to see if we have an area large enough.
        if len(line_info) == 100:
            width = line_info[0][1].x_val - line_info[-1][0].x_val + 1
            if width >= 100:
                return line_info[-1][0].x_val * 10000 + line_info[0][1].y_val


if __name__ == "__main__":
    aoc.main(part1, part2)
