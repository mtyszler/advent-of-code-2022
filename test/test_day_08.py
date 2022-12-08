from functions_day_08 import *


def test_parse_grid():
    grid = parse_grid('input_files/input_day_08_example.txt')
    print(grid)
    assert (grid[3, 3] == 4)
    assert (grid[2, 1] == 5)


def test_visibility_grid():
    grid = parse_grid('input_files/input_day_08_example.txt')
    grid_visibility = visibility_tree(grid)
    print(grid_visibility)

    assert (sum(sum(grid_visibility)) == 21)


def test_scenic_score():
    grid = parse_grid('input_files/input_day_08_example.txt')
    grid_scenic_score = scenic_score(grid)
    print(grid_scenic_score)

    assert (grid_scenic_score.max() == 8)