import pytest

from functions_day_19 import *


def test_parse_cubes():
    blueprints = parse_blueprints('input_files/input_day_19_example.txt')
    print(blueprints)


def test_parse_cubes():
    blueprints = parse_blueprints('input_files/input_day_19_example.txt')

    stones_1 = optimize_blueprint(blueprints[0], minutes=24)
    assert (stones_1 == 9)

#    stones_2 = optimize_blueprint(blueprints[1], minutes=24)
#    assert (stones_2 == 12)
