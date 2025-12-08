#!/bin/python
import sys


class Guard:
    def __init__(self, pos_x=0, pos_y=0, dir_x=0, dir_y=0, icon='^'):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.icon = icon


guard_icons = {
    '<': {'x': 0, 'y': -1},
    '^': {'x': -1, 'y': 0},
    '>': {'x': 0, 'y': 1},
    'v': {'x': 1, 'y': 0}
}


def get_guards_position(grid):
    for x in range(len(grid)):
        row = grid[x]
        for y in range(len(row)):
            column = row[y]
            if column in guard_icons.keys():
                return x, y

    return -1, -1


def get_guard_direction(grid, x, y):
    return grid[x][y]


icp = Guard()


def change_guard_direction():
    icons = list(guard_icons.keys())
    icon_idx = icons.index(icp.icon)

    icon_idx += 1

    icp.icon = icons[icon_idx % len(icons)]
    icp.dir_x = guard_icons[icp.icon]['x']
    icp.dir_y = guard_icons[icp.icon]['y']


def calculate_guards_path(grid):
    elvis_has_left_the_building = False
    path_traced_grid = grid

    while elvis_has_left_the_building is False:
        if 0 > icp.pos_x or icp.pos_x >= len(grid):
            elvis_has_left_the_building = True
            continue
        if 0 > icp.pos_y or icp.pos_y >= len(grid[icp.pos_x]):
            elvis_has_left_the_building = True
            continue

        if grid[icp.pos_x][icp.pos_y] == '#':
            icp.pos_x -= icp.dir_x
            icp.pos_y -= icp.dir_y
            change_guard_direction()

            continue

        path_traced_grid[icp.pos_x][icp.pos_y] = 'X'

        icp.pos_x += icp.dir_x
        icp.pos_y += icp.dir_y

    return path_traced_grid


def count_distinct_positions(traced_grid):
    count = 0
    for x in range(len(traced_grid)):
        for y in range(len(traced_grid[x])):
            if traced_grid[x][y] in ["+", "|", "-"]:
                count += 1

    return count


if __name__ == '__main__':
    input_file_name = sys.argv[1]

    the_grid = []

    with open(input_file_name, "r") as f:
        temp_list = []
        for line in f.read():
            if line == '\n':
                the_grid.append(temp_list)
                temp_list = []
            else:
                temp_list += line.split()
        the_grid.append(temp_list)


    (pos_x, pos_y) = get_guards_position(the_grid)
    direction = get_guard_direction(the_grid, pos_x, pos_y)

    icp.icon = direction
    icp.pos_x = pos_x
    icp.pos_y = pos_y
    icp.dir_x = guard_icons[direction]['x']
    icp.dir_y = guard_icons[direction]['y']

    traced_grid = calculate_guards_path(the_grid)
    distinct_positions = count_distinct_positions(traced_grid)

    print(f"Distinct position the guard will visit: {distinct_positions}")
