import numpy as np


def parse_grid(input_file: str) -> np.ndarray:
    """

    Args:
        input_file:

    Returns:

    """

    with open(input_file, 'r') as f:
        data = f.readlines()

    result = []
    for line in data:
        splitted_data = [int(item) for item in str(line.strip())]

        result.append(splitted_data)

    grid = np.array(result, dtype='i')

    return grid


def visibility_tree(grid: np.ndarray) -> np.ndarray:
    """

    Args:
        grid:

    Returns:

    """

    # initialize
    visibility_grid = -np.ones_like(grid)

    # determine visibility
    it = np.nditer(grid, flags=['multi_index'])
    for x in it:
        if it.multi_index[0] == 0 or it.multi_index[0] == grid.shape[0]-1 or \
                it.multi_index[1] == 0 or it.multi_index[1] == grid.shape[1]-1:
            visibility_grid[it.multi_index] = 1

        else:
            # from top to element
            visibility_grid[it.multi_index] = x > max(grid[0:it.multi_index[0], it.multi_index[1]])
            if visibility_grid[it.multi_index] == 1:
                continue

            # from bottom to element
            visibility_grid[it.multi_index] = x > max(grid[it.multi_index[0]+1:grid.shape[0], it.multi_index[1]])
            if visibility_grid[it.multi_index] == 1:
                continue

            # from left to element
            visibility_grid[it.multi_index] = x > max(grid[it.multi_index[0], 0:it.multi_index[1]])
            if visibility_grid[it.multi_index] == 1:
                continue

            # from right to element
            visibility_grid[it.multi_index] = x > max(grid[it.multi_index[0], it.multi_index[1]+1:grid.shape[1]])
            if visibility_grid[it.multi_index] == 1:
                continue

    return visibility_grid


def scenic_score(grid: np.ndarray) -> np.ndarray:
    """

    Args:
        grid:

    Returns:

    """

    # initialize
    scenic_grid = -np.ones_like(grid)

    # determine visibility
    it = np.nditer(grid, flags=['multi_index'])
    for x in it:
        if it.multi_index[0] == 0 or it.multi_index[0] == grid.shape[0]-1 or \
                it.multi_index[1] == 0 or it.multi_index[1] == grid.shape[1]-1:
            scenic_grid[it.multi_index] = 0

        else:
            # from top to element
            top_match = np.argwhere(grid[0:it.multi_index[0], it.multi_index[1]] >= x)
            try:
                top = it.multi_index[0]-top_match.max()
            except ValueError:
                top = it.multi_index[0]

            # from bottom to element
            bottom_match = np.argwhere(grid[it.multi_index[0]+1:grid.shape[0], it.multi_index[1]] >= x)
            try:
                bottom = bottom_match.min() + 1
            except ValueError:
                bottom = grid.shape[0] - it.multi_index[0] - 1

            # from left to element
            left_match = np.argwhere(grid[it.multi_index[0], 0:it.multi_index[1]] >= x)
            try:
                left = it.multi_index[1]-left_match.max()
            except ValueError:
                left = it.multi_index[1]

            # from right to element
            right_match = np.argwhere(grid[it.multi_index[0], it.multi_index[1]+1:grid.shape[1]] >= x)
            try:
                right = right_match.min() + 1
            except ValueError:
                right = grid.shape[1] - it.multi_index[1] - 1

            scenic_grid[it.multi_index] = left * right * top * bottom

    return scenic_grid
