import pytest

from functions_day_12 import *


def test_parse_height_map():
    grid_height = parse_height_map('input_files/input_day_12_example.txt')


def test_find_top():
    grid_height = parse_height_map('input_files/input_day_12_example.txt')
    top_steps, tracking_grid = find_top_v1(grid_height)
    assert (top_steps == 31)
