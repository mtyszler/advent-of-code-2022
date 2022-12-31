import numpy as np
import pytest

from functions_day_22 import *


def test_decoder():
    matrix = make_matrix('input_files/input_day_22_example.txt')

    print(matrix)


def test_find_endpoint():
    instructions = "10R5L5R10L4R5L5"
    matrix = make_matrix('input_files/input_day_22_example.txt')

    row, col, direction = find_endpoint(matrix, instructions)

    pw = 1000 * row + 4 * col + direction
    assert (pw == 6032)

