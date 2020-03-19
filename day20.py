#!/usr/bin/env python3

from collections import defaultdict, deque, namedtuple
from enum import Enum, auto

import aoc


class Maze:
    # pylint: disable=too-few-public-methods

    INCREMENT = {aoc.Coord(0, 1), aoc.Coord(0, -1), aoc.Coord(-1, 0), aoc.Coord(1, 0)}

    Location = namedtuple('Location', ['level', 'coord'])

    class Type(Enum):
        PLAIN = auto()
        RECURSIVE = auto()

    def __init__(self, input_list, maze_type):
        self._maze_type = maze_type
        self._entrance = None
        self._exit = None

        self._upper_left_coord = aoc.Coord(2, 2)
        self._lower_right_coord = aoc.Coord(len(input_list[0]) - 3, len(input_list) - 3)

        self._maze = {}
        self._portals = defaultdict(list)

        self._parse_input(input_list)

    def _is_inside_portal(self, coord):
        return self._upper_left_coord.x_val < coord.x_val < self._lower_right_coord.x_val and \
               self._upper_left_coord.y_val < coord.y_val < self._lower_right_coord.y_val

    def _is_outside_portal(self, coord):
        return not self._is_inside_portal(coord)

    def _find_portal_exit(self, portal, entrance_location):
        exit_location = None
        portal_info_list = self._portals[portal]
        for portal_info in portal_info_list:
            if portal_info[0] != entrance_location.coord:
                exit_location = self.Location(level=entrance_location.level, coord=portal_info[1])
                break

        if self._maze_type == self.Type.RECURSIVE:
            if self._is_inside_portal(entrance_location.coord):
                exit_location = exit_location._replace(level=exit_location.level + 1)
            else:
                exit_location = exit_location._replace(level=exit_location.level - 1)

        return exit_location

    def _parse_input(self, input_list):
        portal_tiles = self._parse_maze(input_list)
        self._parse_portals(portal_tiles)

    def _parse_maze(self, input_list):
        # Parse the input to the maze.  Save the location and names of portals for pairing.
        portal_tiles = {}

        for y_val, line in enumerate(input_list):
            for x_val, tile in enumerate(line):
                coord = aoc.Coord(x_val, y_val)

                if tile in "#.":
                    self._maze[coord] = tile

                elif tile == " ":
                    # Don't store.
                    pass

                elif tile.isupper():
                    portal_tiles[coord] = tile

                else:
                    assert False

        return portal_tiles

    def _parse_portals(self, portal_tiles):
        # Figure out portal names, locatons, and pairing.
        while portal_tiles:
            (coord1, tile1) = portal_tiles.popitem()
            for increment in self.INCREMENT:
                coord2 = aoc.add_coords(coord1, increment)

                if coord2 in portal_tiles:
                    tile2 = portal_tiles.pop(coord2)
                    if tile1 < tile2:
                        portal = tile1 + tile2
                    else:
                        portal = tile2 + tile1

                    break

            for coord in coord1, coord2:
                for increment in self.INCREMENT:
                    coord_to_check = aoc.add_coords(coord, increment)
                    tile = self._maze.get(coord_to_check, None)

                    if tile == '.':
                        if portal == "AA":
                            self._entrance = self.Location(level=1, coord=coord_to_check)
                            self._maze[coord_to_check] = '#'
                        elif portal == "ZZ":
                            self._exit = self.Location(level=1, coord=coord_to_check)
                            self._maze[coord_to_check] = '#'
                        else:
                            self._maze[coord] = portal
                            self._portals[portal].append((coord, coord_to_check))

                        break  # Really need to break two levels.

    def find_shortest_path(self):

        WorkEntry = namedtuple('WorkEntry', ['location', 'steps'])
        work_queue = deque()

        visited = set()
        visited.add(self._entrance)

        work_queue.append(WorkEntry(location=self._entrance, steps=0))

        while work_queue:
            work_entry = work_queue.popleft()
            for increment in self.INCREMENT:
                new_coord = aoc.add_coords(work_entry.location.coord, increment)
                new_location = work_entry.location._replace(coord=new_coord)

                if new_location in visited:
                    continue

                tile = self._maze.get(new_location.coord, None)

                if new_location == self._exit:
                    work_queue.clear()
                    break

                if tile is None:
                    # This will happen if we try to exit when we are still at the entrance.  Treat
                    # like wall.
                    continue

                if tile == '#':
                    # Wall
                    continue

                if tile == '.':
                    # Move to next square.
                    work_queue.append(WorkEntry(location=new_location, steps=work_entry[1] + 1))
                    visited.add(new_location)

                else:
                    # Portal
                    if self._maze_type == self.Type.RECURSIVE and \
                            new_location.level == 1 and \
                            self._is_outside_portal(new_location.coord):
                        # In RECURSIVE mode outer portals on level 1 are treated like walls.
                        continue

                    new_location = self._find_portal_exit(tile, new_location)
                    work_queue.append(WorkEntry(location=new_location, steps=work_entry[1] + 1))
                    visited.add(new_location)

        return work_entry.steps + 1  # +1 for step into the exit square.


def part1(input_list):
    maze = Maze(input_list, Maze.Type.PLAIN)
    return maze.find_shortest_path()


def part2(input_list):
    maze = Maze(input_list, Maze.Type.RECURSIVE)
    return maze.find_shortest_path()


if __name__ == "__main__":
    aoc.main(part1, part2)
