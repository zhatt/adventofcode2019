import argparse
import sys
from collections import namedtuple
from fractions import Fraction

Coord = namedtuple('Coord', ['x_val', 'y_val'])


def add_coords(*coords):
    assert coords
    x_sum = 0
    y_sum = 0
    for x_val, y_val in coords:
        x_sum += x_val
        y_sum += y_val
    return Coord(x_sum, y_sum)


def distance_manhattan_coords(coord1, coord2):
    return abs(coord2.x_val - coord1.x_val) + abs(coord2.y_val - coord1.y_val)


def min_bound_coord(*coords):
    assert coords
    x_min = coords[0].x_val
    y_min = coords[0].y_val
    for x_val, y_val in coords:
        x_min = min(x_min, x_val)
        y_min = min(y_min, y_val)
    return Coord(x_min, y_min)


def max_bound_coord(*coords):
    assert coords
    x_max = coords[0].x_val
    y_max = coords[0].y_val
    for x_val, y_val in coords:
        x_max = max(x_max, x_val)
        y_max = max(y_max, y_val)
    return Coord(x_max, y_max)


def slope_negy(coord1, coord2):
    """
    Calculate slope for coordinates where positive y goes down.
    """
    if coord1.x_val == coord2.x_val:
        # infinite slope
        return sys.maxsize

    return Fraction(-(coord2.y_val - coord1.y_val), coord2.x_val - coord1.x_val)


def coord_relation_negy(coord1, coord2):
    """
    Calculate relationship for coordinates where positive y goes down.

    Where is coord2 in relation to coord1?
    Returns
    0:  Same location
    1:  coord2 is right of coord1
        coord2 is directly above coord1
    -1:  coord2 is left of coord1
         coord2 is directly below coord1
    """
    if coord1 == coord2:
        result = 0

    elif coord1.x_val != coord2.x_val:
        if coord2.x_val > coord1.x_val:
            result = 1
        else:
            result = -1

    # coord2 is directly above or below coord1.
    elif coord2.y_val < coord1.y_val:
        # Above is considered part of the to the right set.
        result = 1
    else:
        # Above is considered part of the to the left set.
        result = -1

    return result


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int, choices=(1, 2), default=1)
    parser.add_argument('input_file')
    return parser.parse_args()


def main(part1, part2):
    args = parse_args()

    input_list = read_input(args.input_file)

    if args.part == 1:
        output = part1(input_list)
        print(output)
    else:
        output = part2(input_list)
        print(output)


def read_input(file_name):
    input_list = list()

    with open(file_name) as file_iter:
        for line in file_iter:
            input_list.append(line.rstrip('\n'))

    return input_list
