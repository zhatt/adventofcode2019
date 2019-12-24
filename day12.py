#!/usr/bin/env python3

import math
import re
from collections import namedtuple

import aoc

# x, y, and z are independent so we will split them and simulate independently.  MoonData
# holds the data for one planet's x, y, or z position and velocity.
MoonData = namedtuple('MoonData', ['pos', 'vel'])


def parse_input(input_list):
    """
    Parse the moon data.  Returns a tuple of lists of MoonData.  One list for each x, y, and z.
    """
    # Example input data
    # <x=2, y=-10, z=-7>
    regex = r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>'

    moon_data_x = []
    moon_data_y = []
    moon_data_z = []

    for line in input_list:
        match_obj = re.search(regex, line)
        assert match_obj

        moon_data_x.append(MoonData(int(match_obj.group(1)), 0))
        moon_data_y.append(MoonData(int(match_obj.group(2)), 0))
        moon_data_z.append(MoonData(int(match_obj.group(3)), 0))

    moon_data = (moon_data_x, moon_data_y, moon_data_z)
    return moon_data


def simulate_one_step_single_axis(moon_data_list):
    # Compare moon1 to moon2 and update moon1's velocity.  We don't need to worry about excluding
    # compare of moon1 to itself since the algorithm give zero increment for that because the
    # position will be the same.
    for index1, moon1 in enumerate(moon_data_list):
        for moon2 in moon_data_list:
            increment = -1 if moon1.pos > moon2.pos else 1 if moon1.pos < moon2.pos else 0
            moon_data_list[index1] = MoonData(moon_data_list[index1].pos,
                                              moon_data_list[index1].vel + increment)

    # Update moon locations.
    for index, moon in enumerate(moon_data_list):
        moon_data_list[index] = MoonData(moon.pos + moon.vel, moon.vel)


def simulate_one_step(moon_data):
    # for x, y, z lists
    for data in moon_data:
        simulate_one_step_single_axis(data)


def calculate_energy(moon_data):
    energy = 0

    # Need to analyze x, y, z data together because final multiply aggregates all three axes.
    for x_data, y_data, z_data in zip(moon_data[0], moon_data[1], moon_data[2]):
        potential_energy = abs(x_data.pos) + abs(y_data.pos) + abs(z_data.pos)
        kinetic_energy = abs(x_data.vel) + abs(y_data.vel) + abs(z_data.vel)
        energy += potential_energy * kinetic_energy

    return energy


def find_cycle_time_single_axis(moon_data_list):
    """
    Find the time to when position and velocity repeat for the input list of moon data.
    Modifies moon_data_list

    My algorithm assumes that the loop always returns to the original state.  It seems like you
    could have an orbit set that goes for a while and then gets into the loop so that when it
    loops it starts at a later state but that doesn't happen with my input.  I originally did use
    a set to look for that case.
    """
    time = 0

    first_state = moon_data_list.copy()

    while True:
        simulate_one_step_single_axis(moon_data_list)
        time += 1
        new_state = moon_data_list.copy()
        if new_state == first_state:
            break

    return time


def lcm(first, second):
    # Calculate least common multiple
    return abs(first * second) // math.gcd(first, second)


def find_cycle_time(moon_data):
    # Find the cycle time of each axis.  The combined cycle time is the least common multiple of
    # the three cycle times.
    x_cycle = find_cycle_time_single_axis(moon_data[0])
    y_cycle = find_cycle_time_single_axis(moon_data[1])
    z_cycle = find_cycle_time_single_axis(moon_data[2])

    lcm_xy = lcm(x_cycle, y_cycle)
    lcm_xyz = lcm(lcm_xy, z_cycle)

    return lcm_xyz


def part1(input_list):
    moon_data = parse_input(input_list)

    for _ in range(1000):
        simulate_one_step(moon_data)

    energy = calculate_energy(moon_data)

    return energy


def part2(input_list):
    moon_data = parse_input(input_list)
    return find_cycle_time(moon_data)


if __name__ == "__main__":
    aoc.main(part1, part2)
