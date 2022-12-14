import pytest

from functions_day_12 import *


def test_parse_height_map():
    grid_height = parse_height_map('input_files/input_day_12_example.txt')


def test_find_top():
    grid_height = parse_height_map('input_files/input_day_12_example.txt')
    best_distance, best_path = find_top(grid_height)

    route_map = make_route(grid_height, best_path)
    print("route")
    print(route_map)

    assert (best_distance == 31)
