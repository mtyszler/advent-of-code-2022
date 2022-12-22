import pytest

from functions_day_17 import *


def test_tetris():
    matrix = tetris('input_files/input_day_17_example.txt', wide=7, n_rocks=2022)
    i=0
    while sum(matrix[i, :]) == 0:
        i += 1
        if i >= matrix.shape[0]:
            break

    assert(matrix.shape[0]-i == 3068)
