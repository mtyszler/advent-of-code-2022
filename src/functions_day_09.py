import numpy as np


def parse_movements(input_file: str, grid_size: int = 200) -> np.ndarray:
    """

    Args:
        grid_size:
        input_file:

    Returns:
        grid with markers of Tail
    """

    if not (grid_size % 2) == 0:
        raise ValueError("Please provide an even grid_size value")

    # initialize grid
    grid_tail = np.zeros([grid_size, grid_size], dtype='i')

    s = [int(grid_size / 2), int(grid_size / 2)]
    grid_tail[s[0], s[1]] = 1
    T_pos = s.copy()
    H_pos = s.copy()

    with open(input_file, 'r') as f:
        movements = f.readlines()

    for movement in movements:
        direction, amount = movement.strip().split(sep=" ")
        for _ in range(int(amount)):
            H_pos = _apply_movement(H_pos, direction)
            T_pos = _apply_reaction(T_pos, H_pos)
            grid_tail[T_pos[0], T_pos[1]] = 1

    return grid_tail


def _apply_movement(H_pos: [int, int], mov_dir: str) -> [int, int]:
    """

    Args:
        H_pos:
        mov_dir:

    Returns:

    """
    if mov_dir == "R":
        H_pos[1] += 1

    elif mov_dir == "L":
        H_pos[1] -= 1

    elif mov_dir == "D":
        H_pos[0] += 1

    elif mov_dir == "U":
        H_pos[0] -= 1

    else:
        raise ValueError("Unknown direction value")

    return H_pos


def _apply_reaction(T_pos: [int, int], H_pos: [int, int]) -> [int, int]:
    """

    Args:
        T_pos:
        H_pos:

    Returns:

    """

    ed = np.sqrt((T_pos[0]-H_pos[0]) ** 2 + (T_pos[1]-H_pos[1]) ** 2)

    if ed > np.sqrt(2):
        T_pos[0] += 1 * np.sign(H_pos[0] - T_pos[0])
        T_pos[1] += 1 * np.sign(H_pos[1] - T_pos[1])

    return T_pos


def parse_movements_v2(input_file: str, grid_size: int = 200) -> np.ndarray:
    """

    Args:
        grid_size:
        input_file:

    Returns:
        grid with markers of Tail
    """

    if not (grid_size % 2) == 0:
        raise ValueError("Please provide an even grid_size value")

    # initialize grid
    grid_tail = np.zeros([grid_size, grid_size], dtype='i')

    s = [int(grid_size / 2), int(grid_size / 2)]
    grid_tail[s[0], s[1]] = 1
    knots = []
    for i in range(10):
        knots.append(s.copy())

    with open(input_file, 'r') as f:
        movements = f.readlines()

    for movement in movements:
        direction, amount = movement.strip().split(sep=" ")
        for _ in range(int(amount)):
            knots[0] = _apply_movement(knots[0], direction)
            for i in range(1, 10):
                knots[i] = _apply_reaction(knots[i], knots[i - 1])
            grid_tail[knots[9][0], knots[9][1]] = 1

    return grid_tail
