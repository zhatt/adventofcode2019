#!/usr/bin/env python3

from collections import namedtuple
import aoc


class Eris:
    LEVEL_SIZE_X = 5
    LEVEL_SIZE_Y = 5

    def __init__(self, input_list, recursive=False):
        MapData = namedtuple('MapData', ['min_level', 'max_level', 'map'])

        """
        Parse input to a set of coordinate locations.  Only locations with a bugs will be put in
        the map.
        """
        data = set()

        x_loc = 0  # for pylint
        y_loc = 0
        for y_loc, row in enumerate(input_list):
            for x_loc, value in enumerate(row):
                if value == '#':
                    data.add((0, aoc.Coord(x_loc, y_loc)))

        assert x_loc == self.LEVEL_SIZE_X - 1
        assert y_loc == self.LEVEL_SIZE_Y - 1

        self.map_data = MapData(min_level=0, max_level=0, map=frozenset(data))
        self.recursive = recursive

    def get_map_string(self, level):
        string = ""
        for y_index in range(self.LEVEL_SIZE_Y):
            for x_index in range(self.LEVEL_SIZE_X):
                coord = aoc.Coord(x_index, y_index)
                if (level, coord) in self.map_data.map:
                    string += "#"
                else:
                    string += "."

            string += "\n"

        return string

    def calculate_biodiversity(self, level):
        rating = 0
        points = 1
        for y_index in range(self.LEVEL_SIZE_Y):
            for x_index in range(self.LEVEL_SIZE_X):
                coord = aoc.Coord(x_index, y_index)
                if (level, coord) in self.map_data.map:
                    rating += points

                points *= 2

        return rating

    def number_of_bugs(self):
        return len(self.map_data.map)

    def simulate(self):
        new_map = set()

        if self.recursive:
            # In recursive mode we gain two levels each minute
            min_level = self.map_data.min_level - 1
            max_level = self.map_data.max_level + 1
        else:
            min_level = self.map_data.min_level
            max_level = self.map_data.max_level

        for level in range(min_level, max_level + 1):
            for y_index in range(self.LEVEL_SIZE_Y):
                for x_index in range(self.LEVEL_SIZE_X):
                    coord = aoc.Coord(x_index, y_index)

                    # Skip the center square in recursive mode.
                    if self.recursive and coord == aoc.Coord(2, 2):
                        continue

                    adjacent_count = self._count_adjacent(level, coord)

                    if (level, coord) in self.map_data.map:
                        # Bug with exactly one bug adjacent gets to live.
                        if adjacent_count == 1:
                            new_map.add((level, coord))

                    else:
                        # Empty square with 1 or 2 bugs adjacent gets infested.
                        if adjacent_count in (1, 2):
                            new_map.add((level, coord))

        self.map_data = self.map_data._replace(
            min_level=min_level,
            max_level=max_level,
            map=frozenset(new_map)
        )

    def _count_adjacent(self, level, coord):
        # pylint: disable=too-many-branches

        count = 0
        # Check the four adjacent coordinates
        for increment in (aoc.Coord(1, 0), aoc.Coord(-1, 0), aoc.Coord(0, 1), aoc.Coord(0, -1)):
            if (level, aoc.add_coords(coord, increment)) in self.map_data.map:
                count += 1

        if not self.recursive:
            return count

        # Handle special recursion cases.
        # NB.  This can't use elif because some cases like (0,0) need to use two of the if cases
        # for to count both above/below and left/right squares.
        if coord.x_val == 0:
            coord_next_level = aoc.Coord(1, 2)
            if (level - 1, coord_next_level) in self.map_data.map:
                count += 1

        if coord.x_val == self.LEVEL_SIZE_X - 1:
            coord_next_level = aoc.Coord(3, 2)
            if (level - 1, coord_next_level) in self.map_data.map:
                count += 1

        if coord.y_val == 0:
            coord_next_level = aoc.Coord(2, 1)
            if (level - 1, coord_next_level) in self.map_data.map:
                count += 1

        if coord.y_val == self.LEVEL_SIZE_Y - 1:
            coord_next_level = aoc.Coord(2, 3)
            if (level - 1, coord_next_level) in self.map_data.map:
                count += 1

        if coord == aoc.Coord(2, 1):
            for x_val in range(0, self.LEVEL_SIZE_X):
                if (level + 1, aoc.Coord(x_val, 0)) in self.map_data.map:
                    count += 1

        if coord == aoc.Coord(2, 3):
            for x_val in range(0, self.LEVEL_SIZE_X):
                if (level + 1, aoc.Coord(x_val, self.LEVEL_SIZE_Y - 1)) in self.map_data.map:
                    count += 1

        if coord == aoc.Coord(1, 2):
            for y_val in range(0, self.LEVEL_SIZE_Y):
                if (level + 1, aoc.Coord(0, y_val)) in self.map_data.map:
                    count += 1

        if coord == aoc.Coord(3, 2):
            for y_val in range(0, self.LEVEL_SIZE_Y):
                if (level + 1, aoc.Coord(self.LEVEL_SIZE_X - 1, y_val)) in self.map_data.map:
                    count += 1

        return count


def part1(input_list):
    eris = Eris(input_list)

    # Keep track of the states we have seen already.
    seen = set()
    seen.add(eris.get_map_string(level=0))

    # Simulate until we see the same state twice.
    while True:
        eris.simulate()
        map_string = eris.get_map_string(level=0)

        if map_string in seen:
            return eris.calculate_biodiversity(level=0)

        seen.add(map_string)


def part2(input_list):
    # How many bugs after 200 minutes
    eris = Eris(input_list, recursive=True)
    for _ in range(200):
        eris.simulate()
    return eris.number_of_bugs()


if __name__ == "__main__":
    aoc.main(part1, part2)
