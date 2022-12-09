from functions_day_09 import *


def test_parse_grid():
    grid = parse_movements('input_files/input_day_09_example.txt', grid_size=10)
    print(grid)

    assert (sum(sum(grid)) == 13)


def test_parse_grid_v2():
    grid = parse_movements_v2('input_files/input_day_09_example.txt', grid_size=10)
    print(grid)

    assert (sum(sum(grid)) == 1)


def test_parse_grid_v2b():
    grid = parse_movements_v2('input_files/input_day_09b_example.txt', grid_size=100)
    print(grid)

    assert (sum(sum(grid)) == 36)
