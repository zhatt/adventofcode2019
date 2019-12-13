#!/usr/bin/env python3

import aoc


def parse_input(lines):
    map_data = {}
    for line in lines:
        (center, outside) = line.split(')')
        map_data[outside] = center
    return map_data


def get_path_to_com(map_data, orbiting_object):
    path = []

    while orbiting_object != "COM":
        orbiting_object = map_data[orbiting_object]
        path.append(orbiting_object)

    return path


def count_orbits(map_data):
    count = 0

    for orbiting_object in map_data:
        path = get_path_to_com(map_data, orbiting_object)
        count += len(path)

    return count


def get_orbits_apart(map_data, object1, object2):
    path1 = get_path_to_com(map_data, object1)
    path2 = get_path_to_com(map_data, object2)

    path1.reverse()
    path2.reverse()

    # Calculate the length of common part of the path to COM.
    count = 0
    for (first, second) in zip(path1, path2):
        if first == second:
            count += 1
        else:
            break

    # The number of orbits apart is the length of the paths that is not common to both.
    orbits_apart = len(path1) - count + len(path2) - count
    return orbits_apart


def part1(input_list):
    map_data = parse_input(input_list)
    number_of_orbits = count_orbits(map_data)
    return number_of_orbits


def part2(input_list):
    map_data = parse_input(input_list)
    number_of_transfers = get_orbits_apart(map_data, "SAN", "YOU")
    return number_of_transfers


if __name__ == "__main__":
    aoc.main(part1, part2)
