#!/usr/bin/env python3

import aoc
import int_code_computer


class PaintingRobot:

    def __init__(self, int_code, ship, start_color=0):
        self._input_stream = [start_color]
        self._output_stream = []
        self._computer = int_code_computer.IntCodeComputer(int_code, self._input_stream,
                                                           self._output_stream)
        self._direction = aoc.Coord(0, 1)
        self._location = aoc.Coord(0, 0)
        self._ship = ship
        self._paint_used = 0

    def move_forward(self):
        self._location = aoc.add_coords(self._location, self._direction)

    def turn_left_and_move(self):
        next_direction = complex(self._direction.x_val, self._direction.y_val) * complex(0, 1)
        # complex numbers are float so truncate back to int.
        self._direction = aoc.Coord(int(next_direction.real), int(next_direction.imag))
        self.move_forward()

    def turn_right_and_move(self):
        next_direction = complex(self._direction.x_val, self._direction.y_val) * complex(0, -1)
        # complex numbers are float so truncate back to int.
        self._direction = aoc.Coord(int(next_direction.real), int(next_direction.imag))
        self.move_forward()

    def paint(self):
        while not self._computer.is_halted():
            self._computer.run(until=self._computer.OUTPUT)
            if self._computer.is_halted():
                break
            color = self._output_stream.pop(0)
            self._computer.run(until=self._computer.OUTPUT)
            direction = self._output_stream.pop(0)
            self._ship.set_color(self._location, color)
            self._paint_used += 1

            if direction == 0:
                self.turn_left_and_move()
            else:
                self.turn_right_and_move()

            self._input_stream.append(self._ship.get_color(self._location))

        return self._ship.number_of_squares_painted()


class Ship:
    def __init__(self):
        # Hull is a dictionary indexed by Coord().  Defaults to int default of 0 which is black.
        self._hull = dict()

    def get_color(self, coord):
        return self._hull.get(coord, 0)

    def set_color(self, coord, color):
        self._hull[coord] = color

    def number_of_squares_painted(self):
        return len(self._hull)

    def get_hull_pattern(self):
        min_coord = aoc.min_bound_coord(*list(self._hull.keys()))
        max_coord = aoc.max_bound_coord(*list(self._hull.keys()))

        output_string = ""
        for y_index in range(max_coord.y_val, min_coord.y_val - 1, -1):
            for x_index in range(min_coord.x_val, max_coord.x_val + 1):
                if self.get_color(aoc.Coord(x_index, y_index)) == 1:
                    output_string += "*"
                else:
                    output_string += ' '
            output_string += "\n"

        return output_string


def part1(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    ship = Ship()
    robot = PaintingRobot(int_code, ship, start_color=0)

    return robot.paint()


def part2(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    ship = Ship()
    robot = PaintingRobot(int_code, ship, start_color=1)
    robot.paint()

    return ship.get_hull_pattern()


if __name__ == "__main__":
    aoc.main(part1, part2)
