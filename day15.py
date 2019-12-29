#!/usr/bin/env python3
import copy
from collections import deque
from enum import Enum

import aoc
import int_code_computer


class Droid:
    class InputCommand(Enum):
        NORTH = 1
        SOUTH = 2
        WEST = 3
        EAST = 4

    increment = {
        InputCommand.NORTH: aoc.Coord(0, 1),
        InputCommand.SOUTH: aoc.Coord(0, -1),
        InputCommand.WEST: aoc.Coord(-1, 0),
        InputCommand.EAST: aoc.Coord(1, 0),
    }

    class StatusCode(Enum):
        HIT_WALL = 0
        MOVE_COMPLETED = 1
        OXYGEN_LOCATION = 2

    def __init__(self, int_code):
        self._location = aoc.Coord(0, 0)
        self._input_stream = []
        self._output_stream = []

        self.icc = int_code_computer.IntCodeComputer(int_code, self._input_stream,
                                                     self._output_stream)

    def run(self, command):
        self._input_stream.append(command.value)
        self.icc.run(until=self.icc.OUTPUT)
        status = self.StatusCode(self._output_stream[-1])
        if status != self.StatusCode.HIT_WALL:
            self._location = aoc.add_coords(self._location, self.increment[command])

        return status

    def get_location(self):
        return self._location


def find_oxygen_system_and_draw_map(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    # Do a breadth first search of all paths to the oxygen system.  The work queue will
    # contain Droid objects that each with a current path it has walked.  This probably is more
    # space overhead than just keeping track of where it is but that way we don't need to resimulate
    # the full path each time we take a previous path out of the queue.
    #
    # locations_visited is used to keep track of previously visited coordinates.  Since we are
    # doing a breadth first search a previous visit to the coordinate means the previous path is
    # shorter (or equal) in length than the current path so we don't need to continue simulating
    # the current path.
    #
    # Prime the work queue with the starting position which is arbitrarily located at the origin.
    # The actual location doesn't really matter since all moves are relative.
    #
    # We also need to generate a map so instead of ending the search when we find the oxygen
    # system, we continue until all paths are taken.  The locations_visited is actually also
    # a map as it contains all of the open spaces.  Any coordinate not in the map is a wall.

    work_queue = deque()
    work_queue.append((Droid(int_code.copy()), 0))
    locations_visited = {aoc.Coord(0, 0)}
    oxygen_system_location = None
    number_of_steps_to_oxygen_system = None

    while work_queue:
        droid, num_steps = work_queue.popleft()
        for command in Droid.InputCommand:
            new_droid = copy.deepcopy(droid)
            status = new_droid.run(command)

            if status == Droid.StatusCode.OXYGEN_LOCATION and number_of_steps_to_oxygen_system is \
                    None:
                oxygen_system_location = new_droid.get_location()
                number_of_steps_to_oxygen_system = num_steps + 1
                locations_visited.add(new_droid.get_location())

            elif status == Droid.StatusCode.MOVE_COMPLETED:
                if new_droid.get_location() not in locations_visited:
                    work_queue.append((new_droid, num_steps + 1))
                    locations_visited.add(new_droid.get_location())
                else:
                    # Else we got here via a shorter path so we can prune this path.
                    pass

            else:
                # We hit a wall so we can prune this path.
                pass

    return number_of_steps_to_oxygen_system, oxygen_system_location, locations_visited


def simulate_oxygen_flow(oxygen_system_location, open_locations):
    # Do a breadth first search of all paths from the oxygen system.  Since we are doing a breadth
    # first search, the last object removed from the work queue will be the shortest path to the
    # furthest location.

    work_queue = deque()
    work_queue.append((oxygen_system_location, 0))
    locations_visited = {oxygen_system_location}

    while work_queue:
        location, num_steps = work_queue.popleft()
        for increment in Droid.increment.values():
            new_location = aoc.add_coords(location, increment)
            if new_location not in open_locations:
                # Wall
                continue

            if new_location not in locations_visited:
                work_queue.append((new_location, num_steps + 1))
                locations_visited.add(new_location)

    return num_steps


def part1(input_list):
    distance_to_oxygen_system, _, _ = find_oxygen_system_and_draw_map(input_list)
    return distance_to_oxygen_system


def part2(input_list):
    _, oxygen_system_location, open_locations = find_oxygen_system_and_draw_map(input_list)
    return simulate_oxygen_flow(oxygen_system_location, open_locations)


if __name__ == "__main__":
    aoc.main(part1, part2)
