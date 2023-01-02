import numpy as np
import pytest

from functions_day_23 import *


def test_parser():
    initial_state = parse_elephants('input_files/input_day_23_example.txt', buffer=0)

    print(initial_state)


def test_movements():
    initial_state = parse_elephants('input_files/input_day_23_example.txt', buffer=100)

    after = move_elephants(initial_state, n_moves=10)
    print(after)

    # find empty spots
    left = min([x[1] for x in after])
    right = max([x[1] for x in after])
    top = min([x[0] for x in after])
    bottom = max([x[0] for x in after])

    # potential spaces:
    potential = (right-left+1)*(bottom-top+1)

    empty = potential - len(after)
    assert (empty == 110)


def test_movements_v2():
    initial_state = parse_elephants('input_files/input_day_23_example.txt', buffer=100)

    after = move_elephants(initial_state, n_moves=30)
