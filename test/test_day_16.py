import pytest

from functions_day_16 import *


def test_parse_pipes():
    pipes = parse_pipes('input_files/input_day_16_example.txt')


def test_best_route():
    pipes = parse_pipes('input_files/input_day_16_example.txt')
    best_pressure, best_path = best_route(pipes, minutes=30)

    assert (best_pressure == 1651)


def test_best_route_together():
    pipes = parse_pipes('input_files/input_day_16_example.txt')
    best_pressure, best_path = best_route_together(pipes, minutes=26)

    assert (best_pressure == 1707)
