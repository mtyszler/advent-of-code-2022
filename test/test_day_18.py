import pytest

from functions_day_18 import *


def test_parse_cubes():
    cube = parse_cubes('input_files/input_day_18_baby_example.txt', size=2)


def test_baby_example():
    input_file = 'input_files/input_day_18_baby_example.txt'
    cube = parse_cubes(input_file, size=2)
    area = get_surface_area(input_file, cube)
    assert (area == 10)


def test_example():
    input_file = 'input_files/input_day_18_example.txt'
    cube = parse_cubes(input_file, size=6)
    area = get_surface_area(input_file, cube)
    assert (area == 64)


def test_example_v2():
    input_file = 'input_files/input_day_18_example.txt'
    cube = parse_cubes(input_file, size=6)
    area = get_surface_area(input_file, cube)
    air_cubes = find_air_cubes(cube)
    assert (area-sum(sum(sum(air_cubes==0)))*6 == 58)