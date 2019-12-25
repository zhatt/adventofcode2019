#!/usr/bin/env python3
from dataclasses import dataclass, field
from enum import Enum

import aoc
import int_code_computer


@dataclass
class ScreenContents:
    contents: dict = field(default_factory=dict)
    ball_location: aoc.Coord = aoc.Coord(0, 0)
    paddle_location: aoc.Coord = aoc.Coord(0, 0)
    score: int = 0


class TileType(Enum):
    BLANK = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4

    @classmethod
    def glyph(cls, tile_type):
        type_map = {
            cls.BLANK: ' ',
            cls.WALL: '|',
            cls.BLOCK: '*',
            cls.PADDLE: '-',
            cls.BALL: 'o',
        }
        return type_map[TileType(tile_type)]


def update_screen(output_stream, screen_contents):
    """
    :param output_stream: list of integers containing commands from program.
    :param screen_contents:  ScreenContents object to update with output_stream commands.
    """

    for index in range(0, len(output_stream), 3):
        x_pos = output_stream[index]
        y_pos = output_stream[index + 1]
        tile_type_raw = output_stream[index + 2]

        coord = aoc.Coord(x_pos, y_pos)
        if x_pos == -1 and y_pos == 0:
            screen_contents.score = tile_type_raw
        else:
            tile_type = TileType(tile_type_raw)
            screen_contents.contents[coord] = TileType(tile_type_raw)

            if tile_type == TileType.BALL:
                screen_contents.ball_location = coord

            elif tile_type == TileType.PADDLE:
                screen_contents.paddle_location = coord


def draw_screen(screen_contents):
    output_string = ""

    min_coord = aoc.min_bound_coord(*list(screen_contents.contents.keys()))
    max_coord = aoc.max_bound_coord(*list(screen_contents.contents.keys()))

    for y_index in range(max_coord.y_val, min_coord.y_val - 1, -1):
        for x_index in range(min_coord.x_val, max_coord.x_val + 1):
            tile_type = screen_contents.contents[aoc.Coord(x_index, y_index)]
            output_string += TileType.glyph(tile_type)

        output_string += "\n"

    clear_terminal()
    print("SCORE", screen_contents.score)
    print(output_string)


def clear_terminal():
    print(chr(27) + "[2J")


def part1(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    input_stream = []
    output_stream = []
    screen_contents = ScreenContents()

    computer = int_code_computer.IntCodeComputer(int_code, input_stream, output_stream)
    computer.run()
    update_screen(output_stream, screen_contents)

    # Return the number of tiles containing a BLOCK type.
    count = sum(tile_type == TileType.BLOCK for tile_type in screen_contents.contents.values())

    return count


def part2(input_list):
    int_code = int_code_computer.IntCodeComputer.parse_input(input_list[0])

    # Set to free play mode.
    int_code[0] = 2

    input_stream = []
    output_stream = []
    screen_contents = ScreenContents()

    computer = int_code_computer.IntCodeComputer(int_code, input_stream, output_stream)

    while not computer.is_halted():
        computer.run(until=int_code_computer.IntCodeComputer.INPUT)

        update_screen(output_stream, screen_contents)
        output_stream.clear()

        # Uncomment to see the game play.
        ## draw_screen(screen_contents)

        # Move the paddle toward the ball.
        if screen_contents.ball_location.x_val > screen_contents.paddle_location.x_val:
            input_stream.append(1)
        elif screen_contents.ball_location.x_val < screen_contents.paddle_location.x_val:
            input_stream.append(-1)
        else:
            input_stream.append(0)

    return screen_contents.score


if __name__ == "__main__":
    aoc.main(part1, part2)
