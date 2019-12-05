#!/usr/bin/env python3

import aoc
from aoc import Coord


def parse_input(line1, line2):
    path1 = list(line1.split(','))
    path2 = list(line2.split(','))
    return path1, path2


NEXT_INCREMENT = {
    'R': Coord(1, 0),
    'L': Coord(-1, 0),
    'U': Coord(0, 1),
    'D': Coord(0, -1)
}


def simulate(input_list):
    """
    Simulate both part 1 and part 2 at the same time.
    """

    path1, path2 = parse_input(input_list[0], input_list[1])

    # Walk the first wire path and create a map containing the coordinates the first wire touches.
    # We store the minimum length to the coordinate.
    wire_map = {}
    current_coord = Coord(0, 0)
    length = 0

    for segment in path1:
        direction = segment[0]
        distance = int(segment[1:])

        for _ in range(distance):
            length += 1
            current_coord = aoc.add_coords(current_coord, NEXT_INCREMENT[direction])
            if current_coord not in wire_map:
                wire_map[current_coord] = length

    # Walk the second wire path checking for intersections with the first wire.  If we intersect,
    # calculate both the minimum distance to the port (0,0) and the minimum wire length to the
    # intersection.
    current_coord = Coord(0, 0)
    length = 0

    min_distance_from_port = None
    min_length = None

    for segment in path2:
        direction = segment[0]
        distance = int(segment[1:])

        for _ in range(distance):
            length += 1
            current_coord = aoc.add_coords(current_coord, NEXT_INCREMENT[direction])
            if current_coord in wire_map:
                distance_from_port = abs(current_coord.x_val) + abs(current_coord.y_val)

                if min_distance_from_port is None or distance_from_port < min_distance_from_port:
                    min_distance_from_port = distance_from_port

                total_length = wire_map[current_coord] + length
                if min_length is None or total_length < min_length:
                    min_length = total_length

    return min_distance_from_port, min_length


def part1(input_list):
    result, _ = simulate(input_list)
    return result


def part2(input_list):
    _, result = simulate(input_list)
    return result


if __name__ == "__main__":
    aoc.main(part1, part2)
