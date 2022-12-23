import copy

import numpy as np

import sys
sys.path.append('..\src')

from functions_day_17 import *

# # # # challenge 1:
# matrix = tetris('../input_files/input_day_17.txt', wide=7, n_rocks=2022)
# i = 0
# while sum(matrix[i, :]) == 0:
#     i += 1
#     if i >= matrix.shape[0]:
#         break
#
# print("height after 2022")
# print(matrix.shape[0] - i)
# # np.savetxt('tetris_2022.txt', matrix, fmt='%1i')

# part 2
matrix_height = tetris_v2('../input_files/input_day_17.txt', wide=7, n_rocks=1000000000000)
print("height after 1000000000000")
print(matrix_height)
