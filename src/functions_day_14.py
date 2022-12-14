import numpy as np


def parse_cave(input_file: str, col_offset: int = 400, size: int = 200) -> list:
    """

    Args:
        input_file:
        col_offset
        size:

    Returns:
       list of pairs list
    """

    cave = np.zeros([size, size], dtype='i')

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split(sep=' -> ')
        first = True
        for part in parts:
            col, row = part.split(sep=',')
            if first:
                col_left = int(col)
                row_left = int(row)
                first = False
                continue
            cave[min(row_left, int(row)):max(row_left, int(row)) + 1,
                 min(col_left, int(col)) - col_offset:max(col_left, int(col)) + 1 - col_offset] = 1
            col_left = int(col)
            row_left = int(row)

    return cave


def drop_sand(cave: np.ndarray, start_col: int = 100):
    """

    Args:
        cave:
        start_col:

    Returns:

    """

    n_drops = 0
    sum_rows = cave.sum(axis=1)
    for i in range(len(sum_rows)):
        if sum_rows[-i] != 0:
            lowest_row = cave.shape[0] - i
            break
    end_reached = False

    while not end_reached:
        current_row = 0
        current_col = start_col
        is_locked = False

        while not is_locked:

            if cave[current_row + 1, current_col] == 0:
                current_row += 1

            elif cave[current_row + 1, current_col - 1] == 0:
                current_row += 1
                current_col -= 1

            elif cave[current_row + 1, current_col + 1] == 0:
                current_row += 1
                current_col += 1

            else:
                cave[current_row, current_col] = 2
                n_drops += 1
                is_locked = True

            if current_row > lowest_row:
                end_reached = True
                break

    return n_drops, cave


def drop_sand_with_floor(cave: np.ndarray, start_col: int = 100):
    """

    Args:
        cave:
        start_col:

    Returns:

    """

    n_drops = 0
    sum_rows = cave.sum(axis=1)
    for i in range(len(sum_rows)):
        if sum_rows[-i] != 0:
            lowest_row = cave.shape[0] - i
            break

    cave[lowest_row+2, :] = 1

    top_reached = False

    while not top_reached:
        current_row = 0
        current_col = start_col
        is_locked = False

        while not is_locked:

            if cave[current_row + 1, current_col] == 0:
                current_row += 1

            elif cave[current_row + 1, current_col - 1] == 0:
                current_row += 1
                current_col -= 1

            elif cave[current_row + 1, current_col + 1] == 0:
                current_row += 1
                current_col += 1

            else:
                cave[current_row, current_col] = 2
                n_drops += 1
                is_locked = True

            if current_row == 0:
                top_reached = True
                break

    return n_drops, cave

