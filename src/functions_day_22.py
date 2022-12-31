import numpy as np


def make_matrix(input_file: str) -> np.ndarray:
    """

    Args:
        input_file:

    Returns:
      matrix
    """

    fin = open(input_file, "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    data = data.replace(' ', '0')
    data = data.replace('.', '1')
    data = data.replace('#', '2')

    raw_matrix = [[int(x) for x in r] for r in data.split('\n')]
    length = max(map(len, raw_matrix)) + 1  # +1 for right buffer
    matrix = np.array([xi + [0] * (length - len(xi)) for xi in raw_matrix])
    matrix = np.concatenate([np.zeros([1, length], dtype='i'),
                             matrix,
                             np.zeros([1, length], dtype='i')],
                            axis=0)
    # upper and bottom buffer
    matrix = np.concatenate([np.zeros([matrix.shape[0], 1], dtype='i'),
                             matrix],
                            axis=1)

    return matrix


def make_matrix_as_cube(input_file: str, input_file_regions: str) -> [np.ndarray, dict]:
    """

    Args:
        input_file:
        input_file_regions:

    Returns:
      matrix, dictionary about edges
    """

    # matrix
    fin = open(input_file, "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    data = data.replace(' ', '0')
    data = data.replace('.', '1')
    data = data.replace('#', '2')

    raw_matrix = [[int(x) for x in r] for r in data.split('\n')]
    length = max(map(len, raw_matrix)) + 1  # +1 for right buffer
    matrix = np.array([xi + [0] * (length - len(xi)) for xi in raw_matrix])
    matrix = np.concatenate([np.zeros([1, length], dtype='i'),
                             matrix,
                             np.zeros([1, length], dtype='i')],
                            axis=0)
    # upper and bottom buffer
    matrix = np.concatenate([np.zeros([matrix.shape[0], 1], dtype='i'),
                             matrix],
                            axis=1)

    # regions
    fin = open(input_file_regions, "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    data = data.replace(' ', '0')

    raw_matrix_regions = [[int(x) for x in r] for r in data.split('\n')]
    length = max(map(len, raw_matrix_regions)) + 1  # +1 for right buffer
    matrix_regions = np.array([xi + [0] * (length - len(xi)) for xi in raw_matrix_regions])
    matrix_regions = np.concatenate([np.zeros([1, length], dtype='i'),
                                     matrix_regions,
                                     np.zeros([1, length], dtype='i')],
                                    axis=0)
    # upper and bottom buffer
    matrix_regions = np.concatenate([np.zeros([matrix_regions.shape[0], 1], dtype='i'),
                                     matrix_regions],
                                    axis=1)

    edges = {}
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] > 0:
                for neighbour in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:

                    first_col_source = np.nan
                    first_col_dest = np.nan
                    first_row_dest = np.nan
                    first_row_source = np.nan
                    last_row_dest = np.nan
                    row_dest = np.nan
                    col_dest = np.nan

                    if matrix[neighbour[0], neighbour[1]] == 0:
                        if neighbour[0] == i - 1:
                            # 1 --> 6
                            if matrix_regions[i, j] == 1:
                                for first_col_source in range(matrix_regions.shape[1]):
                                    if matrix_regions[i, first_col_source] == 1:
                                        break
                                for dest_row in range(matrix.shape[0]):
                                    if matrix_regions[dest_row, 1] == 6:
                                        break
                                for first_col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[dest_row, first_col_dest] == 6:
                                        break

                                edges[(i, j, 0)] = (dest_row + j - first_col_source, first_col_dest, 90)

                            # 2 --> 6
                            elif matrix_regions[i, j] == 2:
                                for first_col_source in range(matrix_regions.shape[1]):
                                    if matrix_regions[i, first_col_source] == 2:
                                        break
                                found_start = False
                                for dest_row in range(matrix.shape[0]):
                                    if matrix_regions[dest_row, 1] == 6:
                                        found_start = True
                                    if found_start and matrix_regions[dest_row, 1] == 0:
                                        dest_row -= 1
                                        break
                                for first_col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[dest_row, first_col_dest] == 6:
                                        break

                                edges[(i, j, 0)] = (dest_row, first_col_dest + j - first_col_source, 0)

                            # 4 --> 3
                            elif matrix_regions[i, j] == 4:
                                for first_col_source in range(matrix_regions.shape[1]):
                                    if matrix_regions[i, first_col_source] == 4:
                                        break
                                for dest_row in range(matrix.shape[0]):
                                    if matrix_regions[dest_row, 51] == 3:
                                        break
                                for first_col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[dest_row, first_col_dest] == 3:
                                        break

                                edges[(i, j, 0)] = (dest_row + j - first_col_source, first_col_dest, 90)

                        elif neighbour[0] == i + 1:
                            # 2 --> 3
                            if matrix_regions[i, j] == 2:
                                for first_col_source in range(matrix_regions.shape[1]):
                                    if matrix_regions[i, first_col_source] == 2:
                                        break
                                for first_row_dest in range(matrix.shape[0]):
                                    if matrix_regions[first_row_dest, 51] == 3:
                                        break
                                found_start = False
                                for col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[first_row_dest, col_dest] == 3:
                                        found_start = True
                                    if found_start and matrix_regions[first_row_dest, col_dest] == 0:
                                        col_dest -= 1
                                        break

                                edges[(i, j, 180)] = (first_row_dest + j - first_col_source, col_dest, 270)

                            # 5 --> 6
                            elif matrix_regions[i, j] == 5:
                                for first_col_source in range(matrix_regions.shape[1]):
                                    if matrix_regions[i, first_col_source] == 5:
                                        break
                                for first_row_dest in range(matrix.shape[0]):
                                    if matrix_regions[first_row_dest, 1] == 6:
                                        break
                                found_start = False
                                for col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[first_row_dest, col_dest] == 6:
                                        found_start = True
                                    if found_start and matrix_regions[first_row_dest, col_dest] == 0:
                                        col_dest -= 1
                                        break

                                edges[(i, j, 180)] = (first_row_dest + j - first_col_source, col_dest, 270)

                            # 6 --> 2
                            elif matrix_regions[i, j] == 6:
                                for first_col_source in range(matrix_regions.shape[1]):
                                    if matrix_regions[i, first_col_source] == 6:
                                        break
                                for row_dest in range(matrix.shape[0]):
                                    if matrix_regions[row_dest, 101] == 2:
                                        break
                                for first_col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[row_dest, first_col_dest] == 2:
                                        break

                                edges[(i, j, 180)] = (row_dest, first_col_dest + j - first_col_source, 180)

                        elif neighbour[1] == j + 1:

                            # 2 --> 5
                            if matrix_regions[i, j] == 2:
                                for first_row_source in range(matrix_regions.shape[0]):
                                    if matrix_regions[first_row_source, j] == 2:
                                        break
                                found_start = False
                                for last_row_dest in range(matrix.shape[0]):
                                    if matrix_regions[last_row_dest, 51] == 5:
                                        found_start = True
                                    if found_start and matrix_regions[last_row_dest, 51] == 0:
                                        last_row_dest -= 1
                                        break
                                found_start = False
                                for col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[last_row_dest, col_dest] == 5:
                                        found_start = True
                                    if found_start and matrix_regions[last_row_dest, col_dest] == 0:
                                        col_dest -= 1
                                        break

                                edges[(i, j, 90)] = (last_row_dest - (i - first_row_source), col_dest, 270)

                            # 3 --> 2
                            elif matrix_regions[i, j] == 3:
                                for first_row_source in range(matrix_regions.shape[0]):
                                    if matrix_regions[first_row_source, j] == 3:
                                        break
                                found_start = False
                                for last_row_dest in range(matrix.shape[0]):
                                    if matrix_regions[last_row_dest, 101] == 2:
                                        found_start = True
                                    if found_start and matrix_regions[last_row_dest, 101] == 0:
                                        last_row_dest -= 1
                                        break
                                for first_col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[last_row_dest, first_col_dest] == 2:
                                        break

                                edges[(i, j, 90)] = (last_row_dest, first_col_dest + i - first_row_source, 0)

                            # 5 --> 2
                            elif matrix_regions[i, j] == 5:
                                for first_row_source in range(matrix_regions.shape[0]):
                                    if matrix_regions[first_row_source, j] == 5:
                                        break
                                found_start = False
                                for last_row_dest in range(matrix.shape[0]):
                                    if matrix_regions[last_row_dest, 101] == 2:
                                        found_start = True
                                    if found_start and matrix_regions[last_row_dest, 101] == 0:
                                        last_row_dest -= 1
                                        break
                                found_start = False
                                for col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[last_row_dest, col_dest] == 2:
                                        found_start = True
                                    if found_start and matrix_regions[last_row_dest, col_dest] == 0:
                                        col_dest -= 1
                                        break

                                edges[(i, j, 90)] = (last_row_dest - (i - first_row_source), col_dest, 270)

                            # 6 --> 5
                            elif matrix_regions[i, j] == 6:
                                for first_row_source in range(matrix_regions.shape[0]):
                                    if matrix_regions[first_row_source, j] == 6:
                                        break
                                found_start = False
                                for last_row_dest in range(matrix.shape[0]):
                                    if matrix_regions[last_row_dest, 51] == 5:
                                        found_start = True
                                    if found_start and matrix_regions[last_row_dest, 51] == 0:
                                        last_row_dest -= 1
                                        break
                                for first_col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[last_row_dest, first_col_dest] == 5:
                                        break

                                edges[(i, j, 90)] = (last_row_dest, first_col_dest + i - first_row_source, 0)

                        elif neighbour[1] == j - 1:

                            # 1 --> 4
                            if matrix_regions[i, j] == 1:
                                for first_row_source in range(matrix_regions.shape[0]):
                                    if matrix_regions[first_row_source, j] == 1:
                                        break
                                found_start = False
                                for last_row_dest in range(matrix.shape[0]):
                                    if matrix_regions[last_row_dest, 1] == 4:
                                        found_start = True
                                    if found_start and matrix_regions[last_row_dest, 1] == 6:
                                        last_row_dest -= 1
                                        break
                                for col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[last_row_dest, col_dest] == 4:
                                        break

                                edges[(i, j, 270)] = (last_row_dest - (i - first_row_source), col_dest, 90)

                            # 4 --> 1
                            elif matrix_regions[i, j] == 4:
                                for first_row_source in range(matrix_regions.shape[0]):
                                    if matrix_regions[first_row_source, j] == 4:
                                        break
                                found_start = False
                                for last_row_dest in range(matrix.shape[0]):
                                    if matrix_regions[last_row_dest, 51] == 1:
                                        found_start = True
                                    if found_start and matrix_regions[last_row_dest, 51] == 3:
                                        last_row_dest -= 1
                                        break
                                for col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[last_row_dest, col_dest] == 1:
                                        break

                                edges[(i, j, 270)] = (last_row_dest - (i - first_row_source), col_dest, 90)

                            # 3 --> 4
                            elif matrix_regions[i, j] == 3:
                                for first_row_source in range(matrix_regions.shape[0]):
                                    if matrix_regions[first_row_source, j] == 3:
                                        break
                                for row_dest in range(matrix.shape[0]):
                                    if matrix_regions[row_dest, 1] == 4:
                                        break
                                for first_col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[row_dest, first_col_dest] == 4:
                                        break

                                edges[(i, j, 270)] = (row_dest, first_col_dest + i - first_row_source, 180)

                            # 6 --> 1
                            elif matrix_regions[i, j] == 6:
                                for first_row_source in range(matrix_regions.shape[0]):
                                    if matrix_regions[first_row_source, j] == 6:
                                        break
                                for row_dest in range(matrix.shape[0]):
                                    if matrix_regions[row_dest, 51] == 1:
                                        break
                                for first_col_dest in range(matrix_regions.shape[1]):
                                    if matrix_regions[row_dest, first_col_dest] == 1:
                                        break

                                edges[(i, j, 270)] = (row_dest, first_col_dest + i - first_row_source, 180)

    return matrix, edges


def find_endpoint(matrix: np.ndarray, instructions: str) -> [int, int, int]:
    """

    Args:
        matrix:
        instructions:

    Returns:
        row, col , direction (converted)
    """

    # start row:
    row = 1

    # start col:
    for col in range(matrix.shape[1]):
        if matrix[row, col] == 1:
            break

    # start direction
    direction = 90

    # start move_type:
    move_type = "number"

    while len(instructions) > 0:

        # extract next movement
        if move_type == 'letter':
            direction_change = instructions[0]
            instructions = instructions[1:]
            next_move_type = 'number'
        elif move_type == 'number':
            move_amount = ''
            for i in range(len(instructions)):
                if instructions[i].isnumeric():
                    move_amount += instructions[i]
                else:
                    break
            move_amount = eval(move_amount)
            if i + 1 == len(instructions):
                instructions = ''
            else:
                instructions = instructions[i:]
            next_move_type = 'letter'
        else:
            raise ValueError('Unknown movement type')

        # execute movement
        if move_type == 'letter':
            if direction_change == "R":
                direction += 90
                if direction == 360:
                    direction = 0
            elif direction_change == "L":
                direction -= 90
                if direction == -90:
                    direction = 270
            else:
                raise ValueError('Unknown direction change')

        elif move_type == 'number':
            '''
            (' ', '0')
            ('.', '1')
            ('#', '2')
            '''
            for _ in range(move_amount):
                if direction == 90:
                    if matrix[row, col + 1] == 1:
                        col += 1
                    elif matrix[row, col + 1] == 2:
                        break
                    else:
                        for j in range(matrix.shape[1]):
                            if matrix[row, col - j] == 0:
                                if matrix[row, col - j + 1] == 1:
                                    col = col - j + 1
                                    can_continue = True
                                    break
                                elif matrix[row, col - j + 1] == 2:
                                    can_continue = False
                                    break

                        if not can_continue:
                            break

                elif direction == 180:
                    if matrix[row + 1, col] == 1:
                        row += 1
                    elif matrix[row + 1, col] == 2:
                        break
                    else:
                        for j in range(matrix.shape[0]):
                            if matrix[row - j, col] == 0:
                                if matrix[row - j + 1, col] == 1:
                                    row = row - j + 1
                                    can_continue = True
                                    break
                                elif matrix[row - j + 1, col] == 2:
                                    can_continue = False
                                    break

                        if not can_continue:
                            break
                elif direction == 270:
                    if matrix[row, col - 1] == 1:
                        col -= 1
                    elif matrix[row, col - 1] == 2:
                        break
                    else:
                        for j in range(matrix.shape[1]):
                            if matrix[row, col + j] == 0:
                                if matrix[row, col + j - 1] == 1:
                                    col = col + j - 1
                                    can_continue = True
                                    break
                                elif matrix[row, col + j - 1] == 2:
                                    can_continue = False
                                    break

                        if not can_continue:
                            break
                elif direction == 0:
                    if matrix[row - 1, col] == 1:
                        row -= 1
                    elif matrix[row - 1, col] == 2:
                        break
                    else:
                        for j in range(matrix.shape[0]):
                            if matrix[row + j, col] == 0:
                                if matrix[row + j - 1, col] == 1:
                                    row = row + j - 1
                                    can_continue = True
                                    break
                                elif matrix[row + j - 1, col] == 2:
                                    can_continue = False
                                    break

                        if not can_continue:
                            break
                else:
                    raise ValueError('Unknown direction')

        else:
            raise ValueError('Unknown move_type')

        move_type = next_move_type

    # FINAL: row, col, direction

    final_row = row
    final_col = col
    final_direction = int(direction / 90 - 1) if direction != 0 else 3

    return final_row, final_col, final_direction


def find_endpoint_v2(matrix: np.ndarray, instructions: str, edges: dict) -> [int, int, int]:
    """

    Args:
        matrix:
        instructions:
        edges:

    Returns:
        row, col , direction (converted)
    """

    # start row:
    row = 1

    # start col:
    for col in range(matrix.shape[1]):
        if matrix[row, col] == 1:
            break

    # start direction
    direction = 90

    # start move_type:
    move_type = "number"

    while len(instructions) > 0:

        # extract next movement
        if move_type == 'letter':
            direction_change = instructions[0]
            instructions = instructions[1:]
            next_move_type = 'number'
        elif move_type == 'number':
            move_amount = ''
            for i in range(len(instructions)):
                if instructions[i].isnumeric():
                    move_amount += instructions[i]
                else:
                    break
            move_amount = eval(move_amount)
            if i + 1 == len(instructions):
                instructions = ''
            else:
                instructions = instructions[i:]
            next_move_type = 'letter'
        else:
            raise ValueError('Unknown movement type')

        # execute movement
        if move_type == 'letter':
            if direction_change == "R":
                direction += 90
                if direction == 360:
                    direction = 0
            elif direction_change == "L":
                direction -= 90
                if direction == -90:
                    direction = 270
            else:
                raise ValueError('Unknown direction change')

        elif move_type == 'number':
            '''
            (' ', '0')
            ('.', '1')
            ('#', '2')
            '''
            for _ in range(move_amount):
                if direction == 90:
                    if matrix[row, col + 1] == 1:
                        col += 1
                    elif matrix[row, col + 1] == 2:
                        break
                    else:
                        new_tuple = edges[(row, col, direction)]
                        new_row = new_tuple[0]
                        new_col = new_tuple[1]
                        new_direction = new_tuple[2]

                        if matrix[new_row, new_col] == 2:
                            break
                        else:
                            row = new_row
                            col = new_col
                            direction = new_direction

                elif direction == 180:
                    if matrix[row + 1, col] == 1:
                        row += 1
                    elif matrix[row + 1, col] == 2:
                        break
                    else:
                        new_tuple = edges[(row, col, direction)]
                        new_row = new_tuple[0]
                        new_col = new_tuple[1]
                        new_direction = new_tuple[2]

                        if matrix[new_row, new_col] == 2:
                            break
                        else:
                            row = new_row
                            col = new_col
                            direction = new_direction

                elif direction == 270:
                    if matrix[row, col - 1] == 1:
                        col -= 1
                    elif matrix[row, col - 1] == 2:
                        break
                    else:
                        new_tuple = edges[(row, col, direction)]
                        new_row = new_tuple[0]
                        new_col = new_tuple[1]
                        new_direction = new_tuple[2]

                        if matrix[new_row, new_col] == 2:
                            break
                        else:
                            row = new_row
                            col = new_col
                            direction = new_direction

                elif direction == 0:
                    if matrix[row - 1, col] == 1:
                        row -= 1
                    elif matrix[row - 1, col] == 2:
                        break
                    else:
                        new_tuple = edges[(row, col, direction)]
                        new_row = new_tuple[0]
                        new_col = new_tuple[1]
                        new_direction = new_tuple[2]

                        if matrix[new_row, new_col] == 2:
                            break
                        else:
                            row = new_row
                            col = new_col
                            direction = new_direction

                else:
                    raise ValueError('Unknown direction')

        else:
            raise ValueError('Unknown move_type')

        move_type = next_move_type

    # FINAL: row, col, direction

    final_row = row
    final_col = col
    final_direction = int(direction / 90 - 1) if direction != 0 else 3

    return final_row, final_col, final_direction
