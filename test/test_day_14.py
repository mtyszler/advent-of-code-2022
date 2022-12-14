import pytest

from functions_day_14 import *


def test_parse_cave():
    cave = parse_cave('input_files/input_day_14_example.txt')


def test_drops():
    cave = parse_cave('input_files/input_day_14_example.txt')

    n_drops, cave_filled = drop_sand(cave)

    assert (n_drops == 24)


def test_drops_with_bottom():
    cave = parse_cave('input_files/input_day_14_example.txt')

    n_drops, cave_filled = drop_sand_with_floor(cave)

    assert (n_drops == 93)
