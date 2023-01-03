import numpy as np
import pytest

from functions_day_24 import *


def test_parser():
    initial_state = parse_cave('input_files/input_day_24_baby_example.txt')

    print(initial_state)


def test_movements():
    initial_state = parse_cave('input_files/input_day_24_example.txt')


    left = min([coord[0] for coord in initial_state.keys()]) + 1
    right = max([coord[0] for coord in initial_state.keys()]) - 1
    top = min([coord[1] for coord in initial_state.keys()]) + 1
    bottom = max([coord[1] for coord in initial_state.keys()]) - 1

    matrix = np.chararray([bottom+2, right+2])
    for k,v in initial_state.items():
        matrix[k[1],k[0]]=v[0]

    print("")
    print(matrix)

    movements = move_in_cave(initial_state)
    print(movements)
