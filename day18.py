#!/usr/bin/env python3
from collections import deque
from collections import namedtuple

import aoc

VaultMap = namedtuple("VaultMap", ['map', 'entrance', 'number_of_keys'])


def parse_input(input_list):
    entrance = None
    number_of_keys = 0
    vault_map = {}
    for y_loc, line in enumerate(input_list):
        for x_loc, tile in enumerate(line):
            coord = aoc.Coord(x_loc, y_loc)
            vault_map[coord] = tile

            if tile == '@':
                entrance = coord

            if tile.islower():
                number_of_keys += 1

    return VaultMap(vault_map, entrance, number_of_keys)


Visited = namedtuple("Visited", ["location", "keys_found"])

INCREMENT = {aoc.Coord(0, 1), aoc.Coord(0, -1), aoc.Coord(-1, 0), aoc.Coord(1, 0)}


def make_vault_map_four(vault_map):
    for increment in INCREMENT:
        location = aoc.add_coords(vault_map.entrance, increment)
        vault_map.map[location] = '#'

    maps = []
    for increment in aoc.Coord(1, 1), aoc.Coord(-1, 1), aoc.Coord(-1, -1), aoc.Coord(1, -1):
        entrance = aoc.add_coords(vault_map.entrance, increment)
        new_map = vault_map._replace(entrance=entrance)
        maps.append(new_map)

    return maps


WorkQueueEntry = namedtuple("WorkQueueEntryFour", [
    "number_of_steps",  # combined total for all robots
    "active_robot",  # 0-3 or max robot
    "locations",  # Tuple of 1 location per robot
    "keys_found",  # combined set for all robots
])


def get_all_keys(vault_maps):
    number_of_robots = len(vault_maps)

    entrance_locations = tuple(vault_maps[i].entrance for i in range(number_of_robots))

    work_queue = deque()
    locations_visited = []
    for robot in range(number_of_robots):
        work_queue.append(
            WorkQueueEntry(
                number_of_steps=0,
                active_robot=robot,
                locations=entrance_locations,
                keys_found=set(),
            )
        )

        locations_visited.append(set())
        locations_visited[robot].add(
            Visited(location=entrance_locations[robot], keys_found=frozenset()))

    while work_queue:
        work_entry = work_queue.popleft()

        # Try to move the current robot each direction.
        for increment in INCREMENT:
            new_location = aoc.add_coords(work_entry.locations[work_entry.active_robot],
                                          increment)
            new_tile = vault_maps[work_entry.active_robot].map[new_location]
            new_keys_found = work_entry.keys_found.copy()
            new_number_of_steps = work_entry.number_of_steps + 1

            new_locations_list = list(work_entry.locations)
            new_locations_list[work_entry.active_robot] = new_location
            new_locations = tuple(new_locations_list)

            if new_tile.islower() and not new_tile in new_keys_found:
                new_keys_found.add(new_tile)

            new_visited = Visited(new_location, frozenset(new_keys_found))

            if new_visited in locations_visited[work_entry.active_robot]:
                continue

            if new_tile == '#':
                # Wall
                continue

            if new_tile.isupper() and new_tile.lower() not in new_keys_found:
                # Locked door
                continue

            locations_visited[work_entry.active_robot].add(new_visited)

            for robot in range(number_of_robots):
                work_queue.append(
                    WorkQueueEntry(
                        number_of_steps=new_number_of_steps,
                        active_robot=robot,
                        locations=new_locations,
                        keys_found=new_keys_found,
                    )
                )

            if len(new_keys_found) == vault_maps[0].number_of_keys:
                # Found all of the keys.
                work_queue.clear()
                break

    return new_number_of_steps


def part1(input_list):
    vault_map = parse_input(input_list)
    vault_maps = [vault_map]
    num_steps = get_all_keys(vault_maps)
    return num_steps


def part2(input_list):
    vault_map = parse_input(input_list)
    vault_maps = make_vault_map_four(vault_map)
    num_steps = get_all_keys(vault_maps)
    return num_steps


if __name__ == "__main__":
    aoc.main(part1, part2)
