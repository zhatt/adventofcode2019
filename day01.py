#!/usr/bin/env python3

import aoc

def fuel_required_per_mass( mass ):
    return mass // 3 - 2

def fuel_required( mass ):

    total_fuel = 0

    while True:
        fuel = fuel_required_per_mass( mass )
        if fuel > 0:
            total_fuel += fuel
            mass = fuel
        else:
            break

    return total_fuel


def part1( input_list ):
    """
    Calculate fuel mass for ship.
    """

    total_fuel_required = 0

    for mass in input_list:
        total_fuel_required += fuel_required_per_mass( int( mass ) )

    return total_fuel_required


def part2( input_list ):
    """
    Calculate fuel mass for ship and added fuel.
    """

    total_fuel_required = 0

    for mass in input_list:
        total_fuel_required += fuel_required( int( mass ) )

    return total_fuel_required


if __name__ == "__main__":
    aoc.main( part1, part2 )
