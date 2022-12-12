import numpy as np


def parse_height_map(input_file: str) -> np.ndarray:
    """

    Args:
        input_file:

    Returns:
       list of dict of monkey attributes
    """

    with open(input_file, 'r') as f:
        first_line = f.readline().strip('\n')

    n = len(first_line)

    grid_height = np.genfromtxt(input_file, dtype="U1",
                                delimiter=np.ones(n, dtype='i'))

    return grid_height


def find_top_v1(grid_height: np.ndarray):
    """

    Args:
        grid_height:

    Returns:

    """

    tracking_grid = np.zeros_like(grid_height, dtype='i')
    """
     0: not visited cell
    -100: visited cell
    # -2: revisited cell (should not visit again)
    """

    start_location = np.argwhere(grid_height == 'S')
    current_row = start_location[0][0]
    current_col = start_location[0][1]

    step_counter = 0
    tracking_grid[current_row, current_col] += -100
    while grid_height[current_row, current_col] != 'E':
        current_row, current_col = _next_move_v1(grid_height, tracking_grid,
                                                 current_row, current_col)
        tracking_grid[current_row, current_col] += -100
        step_counter += 1
        if np.mod(step_counter, 10) == 0:
            print("step(", np.nanmin(tracking_grid),")")

    return step_counter, tracking_grid


def _next_move_v1(grid_height: np.ndarray, tracking_grid: np.ndarray,
                  current_row: int, current_col: int) -> [int, int]:
    """
    Pseudo Code:

    * Scan each possible position
    * Check tracking grid
    ** If TOP found go there, else
    ** Search for unvisited 1 higher step, else
    ** Search for unvisited same height, else
    ** Search for unvisited lower height...

    Args:
        grid_height:
        tracking_grid:
        current_row:
        current_col:

    Returns:

    """

    """
    check directions:
     1: one step higher (preferred)
     0: same level (next best), START
    -1: step lower 
    NAN: Out of bounds
    NAN: too high (>1 higher)
    """

    direction = np.zeros(4)
    tracking = np.zeros(4)
    """
    0: right
    1: down
    2: left
    3: up
    """
    current_letter = grid_height[current_row, current_col]
    current_value = 1 if current_letter == "S" else ord(current_letter) - 96

    # assess each direction
    # right:
    if current_col == grid_height.shape[1] - 1:
        direction[0] = np.nan
    else:
        next_letter = grid_height[current_row, current_col + 1]
        direction[0] = _eval_letter(current_value, next_letter)
        tracking[0] = tracking_grid[current_row, current_col + 1]

    # down:
    if current_row == grid_height.shape[0] - 1:
        direction[1] = np.nan
    else:
        next_letter = grid_height[current_row + 1, current_col]
        direction[1] = _eval_letter(current_value, next_letter)
        tracking[1] = tracking_grid[current_row + 1, current_col]

    # left:
    if current_col == 0:
        direction[2] = np.nan
    else:
        next_letter = grid_height[current_row, current_col - 1]
        direction[2] = _eval_letter(current_value, next_letter)
        tracking[2] = tracking_grid[current_row, current_col - 1]

    # up:
    if current_row == 0:
        direction[3] = np.nan
    else:
        next_letter = grid_height[current_row - 1, current_col]
        direction[3] = _eval_letter(current_value, next_letter)
        tracking[3] = tracking_grid[current_row - 1, current_col]

    # choose:
    best_direction = np.nanargmax(direction+tracking)
    if np.nanmax(direction+tracking) < 0:
        # raise ValueError("I'm stuck")
        pass
    if best_direction == 0:
        return current_row, current_col + 1
    elif best_direction == 1:
        return current_row + 1, current_col
    elif best_direction == 2:
        return current_row, current_col - 1
    elif best_direction == 3:
        return current_row - 1, current_col


def _eval_letter(current_value: int, next_letter: str) -> int:
    """

    Args:
        current_value:
        next_letter:

    Returns:
         1: one step higher (preferred)
         0: same level (next best), START
        -1: step lower
        NAN: Out of bounds
        NAN: too high (>1 higher)

    """

    if next_letter == "E":
        next_value_diff = ord('z') - 96 - current_value
    elif next_letter == "S":
        next_value_diff = ord('a') - 96 - current_value
    else:
        next_value_diff = ord(next_letter) - 96 - current_value

    if next_value_diff > 1:
        return np.nan
    else:
        return next_value_diff
