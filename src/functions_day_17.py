import copy
from copy import deepcopy
import numpy as np


def tetris(input_file: str, wide: int, n_rocks: int) -> np.ndarray:
    """

    Args:
        input_file:
        wide:
        n_rocks

    Returns:
      matrix with the pieces
    """

    # rocks
    rock_min = np.ones([1, 4], dtype='i')

    rock_plus = np.ones([3, 3], dtype='i')
    rock_plus[0, 0] = 0
    rock_plus[2, 0] = 0
    rock_plus[0, 2] = 0
    rock_plus[2, 2] = 0

    rock_L = np.ones([3, 3], dtype='i')
    rock_L[0:2, 0:2] = 0

    rock_I = np.ones([4, 1], dtype='i')

    rock_square = np.ones([2, 2], dtype='i')

    rocks_order = [rock_min, rock_plus, rock_L, rock_I, rock_square]

    jet_stream = open(input_file, 'r').read()

    # initialize
    matrix = np.zeros([0, wide], dtype='i')
    index_rock = -1
    n_this_rock = 0
    jet_pos = -1

    while n_this_rock < n_rocks:

        n_this_rock += 1
        can_go = True
        jet = True

        index_rock += 1
        if index_rock == 5:
            index_rock = 0
        this_rock = rocks_order[index_rock].copy()

        # find the highest rock:
        if matrix.shape[0] == 0:
            # nothing
            new_top_row = -4

        else:
            i = 0
            while sum(matrix[i, :]) == 0:
                i += 1

            # i - 4 = x -> bottom of the next shape
            # x - this_rock.shape[0] + 1 = y -> top row
            new_top_row = i - 4 - this_rock.shape[0] + 1

        if new_top_row < 0:
            matrix = np.concatenate((np.zeros([-new_top_row, wide], dtype='i'), matrix), axis=0)
            top_left_rock = [0, 2]
        else:
            top_left_rock = [new_top_row, 2]

        while can_go:
            matrix_rock = np.zeros_like(matrix, dtype='i')
            matrix_rock[top_left_rock[0]:top_left_rock[0] + this_rock.shape[0],
                        top_left_rock[1]:top_left_rock[1] + this_rock.shape[1]] = this_rock

            if (matrix + matrix_rock).max() > 1:
                if jet:
                    can_go = False
                    matrix_rock = np.zeros_like(matrix, dtype='i')
                    top_left_rock = old_top_left.copy()
                    matrix_rock[top_left_rock[0]:top_left_rock[0] + this_rock.shape[0],
                                top_left_rock[1]:top_left_rock[1] + this_rock.shape[1]] = this_rock
                    matrix = matrix + matrix_rock

                    continue
                else:
                    top_left_rock = old_top_left.copy()

            old_top_left = top_left_rock.copy()

            if jet:
                # jet stream movement
                jet_pos += 1
                if jet_pos >= len(jet_stream):
                    jet_pos = 0

                movement = jet_stream[jet_pos]

                if movement == ">":
                    if top_left_rock[1] + this_rock.shape[1] >= wide:
                        pass
                    else:
                        top_left_rock[1] += 1
                elif movement == "<":
                    if top_left_rock[1] == 0:
                        pass
                    else:
                        top_left_rock[1] -= 1

                jet = False

            else:
                # downwards movement
                if top_left_rock[0] + this_rock.shape[0] >= matrix.shape[0]:
                    can_go = False
                    matrix_rock = np.zeros_like(matrix, dtype='i')
                    top_left_rock = old_top_left.copy()
                    matrix_rock[top_left_rock[0]:top_left_rock[0] + this_rock.shape[0],
                                top_left_rock[1]:top_left_rock[1] + this_rock.shape[1]] = this_rock
                    matrix = matrix + matrix_rock

                    continue
                else:
                    top_left_rock[0] += 1
                jet = True

    return matrix
