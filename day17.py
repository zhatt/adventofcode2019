#!/usr/bin/env python3
from collections import namedtuple
from enum import Enum
from typing import List

import aoc
import int_code_computer

VERBOSE = False


class VacuumRobot:
    class Mode(Enum):
        CAMERA_ONLY = 1
        MOVEMENT = 2

    def __init__(self, int_code: List[int], mode: Mode) -> None:
        self._input_stream: List[int] = []
        self._output_stream: List[int] = []
        my_int_code = int_code.copy()
        my_int_code[0] = mode.value
        self._computer = int_code_computer.IntCodeComputer(my_int_code, self._input_stream,
                                                           self._output_stream)

    def set_movement_routines(self, movement_routines):
        self._input_stream += movement_routines

    def run(self):
        self._computer.run()
        return self._output_stream[-1]

    def get_camera_output(self):
        # Convert list of int to ASCII string.
        camera_output = "".join(map(chr, self._output_stream))
        self._output_stream.clear()
        return camera_output


def make_scaffolding_map(camera_output):
    # Returns a map of tile contents indexed by Coord and the robot location.

    x_val = 0
    y_val = 0
    scaffolding_map = {}
    robot_location = None

    for map_tile in camera_output:
        if map_tile in "><^v":
            robot_location = aoc.Coord(x_val, y_val)

        if map_tile == "\n":
            y_val += 1
            x_val = 0
        else:
            scaffolding_map[aoc.Coord(x_val, y_val)] = map_tile
            x_val += 1

    return scaffolding_map, robot_location


def calculate_calibration_sum(scaffolding_map):
    calibration_sum = 0

    for coord, contents in scaffolding_map.items():
        # Only check scaffolding locations.
        if contents != "#":
            continue

        # An intersection will have scaffolding on all four sides.
        num_connections = 0
        for increment in (aoc.Coord(-1, 0), aoc.Coord(1, 0), aoc.Coord(0, -1), aoc.Coord(0, 1)):
            coord_to_check = aoc.add_coords(coord, increment)
            if scaffolding_map.get(coord_to_check, "X") == "#":
                num_connections += 1

        # Found an intersection.  Add its value to the calibration.
        if num_connections == 4:
            calibration_sum += coord.x_val * coord.y_val

    return calibration_sum


MoveEntry = namedtuple('MoveEntry', ['next_direction', 'command', 'increment'])
MOVEMENT = {
    '^': (
        MoveEntry('^', None, aoc.Coord(0, -1)),
        MoveEntry('>', 'R', aoc.Coord(1, 0)),
        MoveEntry('<', 'L', aoc.Coord(-1, 0))
    ),
    '>': (
        MoveEntry('>', None, aoc.Coord(1, 0)),
        MoveEntry('v', 'R', aoc.Coord(0, 1)),
        MoveEntry('^', 'L', aoc.Coord(0, -1))
    ),
    'v': (
        MoveEntry('v', None, aoc.Coord(0, 1)),
        MoveEntry('<', 'R', aoc.Coord(-1, 0)),
        MoveEntry('>', 'L', aoc.Coord(1, 0))
    ),
    '<': (
        MoveEntry('<', None, aoc.Coord(-1, 0)),
        MoveEntry('^', 'R', aoc.Coord(0, -1)),
        MoveEntry('v', 'L', aoc.Coord(0, 1))
    ),
}


def calculate_path(scaffolding_map, robot_location):
    path = []

    # Figure out initial turn if needed.  We always turn right.  If we are really tight on program
    # space this can be optimized to do a 'L' instead of 'R', 'R', 'R' when it is closer to turn
    # left.
    robot_direction = scaffolding_map[robot_location]

    while True:
        # Can we move forward?
        movements = MOVEMENT[robot_direction]
        move = movements[0]  # Go forward.
        next_robot_location = aoc.add_coords(robot_location, move.increment)

        if scaffolding_map.get(next_robot_location, '.') == '#':
            # Can move forward.
            break

        # We can't move forward so turn right and try again.
        move = movements[1]
        robot_direction = move.next_direction
        path.append(move.command)

    distance = 0
    moving = True
    while moving:
        moving = False

        movements = MOVEMENT[robot_direction]
        for move in movements:
            next_robot_location = aoc.add_coords(robot_location, move.increment)
            next_robot_direction = move.next_direction

            if scaffolding_map.get(next_robot_location, '.') == '#':
                if move.command is not None:
                    path.append(str(distance))
                    path.append(move.command)
                    # We turned and moved 1 when we start in a new direction.
                    distance = 1
                else:
                    # Moved forward 1 in the existing direction.
                    distance += 1
                robot_location = next_robot_location
                robot_direction = next_robot_direction
                moving = True
                break

        if not moving:
            path.append(str(distance))

    return path


def create_movement_routines(path):
    # I did this visually instead of coding it so it only works for my input.
    if VERBOSE:
        print(path)

    master_command = "A,B,A,C,A,B,C,A,B,C\n"
    command_a = "R,12,R,4,R,10,R,12\n"
    command_b = "R,6,L,8,R,10\n"
    command_c = "L,8,R,4,R,4,R,6\nn\n"

    master_command = list(map(ord, master_command))
    command_a = list(map(ord, command_a))
    command_b = list(map(ord, command_b))
    command_c = list(map(ord, command_c))

    commands = master_command + command_a + command_b + command_c

    return commands


def initialize_robot_and_take_picture(int_code):
    robot = VacuumRobot(int_code, VacuumRobot.Mode.CAMERA_ONLY)
    robot.run()

    camera_output = robot.get_camera_output()
    if VERBOSE:
        print(camera_output)

    return camera_output


def part1(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    camera_output = initialize_robot_and_take_picture(int_code)

    scaffolding_map, _ = make_scaffolding_map(camera_output)

    calibration_sum = calculate_calibration_sum(scaffolding_map)

    return calibration_sum


def part2(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    camera_output = initialize_robot_and_take_picture(int_code)

    scaffolding_map, robot_location = make_scaffolding_map(camera_output)

    path = calculate_path(scaffolding_map, robot_location)
    movement_routines = create_movement_routines(path)

    robot = VacuumRobot(int_code, VacuumRobot.Mode.MOVEMENT)
    robot.set_movement_routines(movement_routines)
    amount_of_dust = robot.run()

    return amount_of_dust


if __name__ == "__main__":
    aoc.main(part1, part2)
