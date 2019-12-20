#!/usr/bin/env python3

from collections import namedtuple
import aoc

DistLoc = namedtuple('DistLoc', ['distance', 'location'])
Slope = namedtuple('DistLoc', ['relation', 'slope'])


def parse_input(input_list):
    """
    Parse input to a set of coordinate locations.  Only locations with an asteroid will be put in
    the map.
    """
    asteroid_map = set()

    for y_loc, row in enumerate(input_list):
        for x_loc, value in enumerate(row):
            if value == '#':
                asteroid_map.add(aoc.Coord(x_loc, y_loc))

    return asteroid_map


def calculate_slopes(base_location, asteroid_map):
    """
    Calculate the slopes of all asteroids in the map referenced to base_location.  If two
    asteroids have the same slope then the closest one will block the view of the further ones.
    """
    slopes = {}

    for location in asteroid_map:
        relation = aoc.coord_relation_negy(base_location, location)
        if relation != 0:
            distance = aoc.distance_manhattan_coords(location, base_location)
            location_list = slopes.setdefault((relation, aoc.slope_negy(base_location,
                                                                        location)), [])
            # Add a tuple containing the distance.  Since distance will be unique we can then
            # sort the list to get a closest to furthest list.
            location_list += [DistLoc(distance, location)]
            location_list.sort()

    return slopes


def find_best_location(asteroid_map):
    """
    Find the asteroid that is situated such that it can see the most other asteroids.
    """
    best_num_asteroids = 0
    best_location = None
    for base_location in asteroid_map:
        slope_set = calculate_slopes(base_location, asteroid_map)
        num_asteroids_seen = len(slope_set)

        if num_asteroids_seen > best_num_asteroids:
            best_num_asteroids = num_asteroids_seen
            best_location = base_location

    return best_location, best_num_asteroids


def simulate_destroying_asteroids(asteroid_map):
    num_asteroids_destroyed = 0

    best_location, _ = find_best_location(asteroid_map)
    slope_set = calculate_slopes(best_location, asteroid_map)

    while num_asteroids_destroyed < 200:
        clockwise_ordered_list = sorted(slope_set, reverse=True)
        for slope in clockwise_ordered_list:
            location_list = slope_set[slope]

            location = location_list.pop(0)
            if not location_list:
                # All locations on this slope are used so drop it.
                slope_set.pop(slope)

            num_asteroids_destroyed += 1

            if num_asteroids_destroyed == 200:
                break

    return location.location.x_val * 100 + location.location.y_val


def part1(input_list):
    asteroid_map = parse_input(input_list)

    _, best_num_asteroids = find_best_location(asteroid_map)
    return best_num_asteroids


def part2(input_list):
    asteroid_map = parse_input(input_list)

    return simulate_destroying_asteroids(asteroid_map)


if __name__ == "__main__":
    aoc.main(part1, part2)
