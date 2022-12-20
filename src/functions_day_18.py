import copy
from copy import deepcopy
import numpy as np


def parse_cubes(input_file: str, size: int) -> np.ndarray:
    """

    Args:
        input_file:
        size:

    Returns:
      3D matrix with the cube
    """

    cube = np.zeros([size, size, size], dtype='i')

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        x, y, z = line.strip().split(",")
        cube[int(y) - 1, int(x) - 1, int(z) - 1] = 1

    return cube


def get_surface_area(input_file: str, cube: np.ndarray):
    """

    Args:
        input_file:
        cube:

    Returns:

    """
    s_area = 0
    N = cube.shape[0]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        x, y, z = line.strip().split(",")
        x = int(x) - 1
        y = int(y) - 1
        z = int(z) - 1

        total_neighbors = 0
        possible_neighbors = [(y + 1, x, z), (y - 1, x, z), (y, x + 1, z),
                              (y, x - 1, z), (y, x, z + 1), (y, x, z - 1)]

        # For each possible neighboring coord, if it doesn't have a neighbor
        # then increase the surface area by 1
        for p in possible_neighbors:
            if p[0] < 0 or p[1] < 0 or p[2] < 0:
                total_neighbors += 1
            elif p[0] >= N or p[1] >= N or p[2] >= N:
                total_neighbors += 1
            elif cube[p] == 0:
                total_neighbors += 1

        s_area += total_neighbors

    return s_area


def find_air_cubes(cube: np.ndarray):
    """

    Args:
        cube:

    Returns:

    """

    N = cube.shape[0]
    new_cube = copy.deepcopy(cube)

    to_check = [(0, 0, 0), (0, 0, N - 1),
                (0, N - 1, 0), (0, N - 1, N - 1),
                (N - 1, 0, 0), (N - 1, 0, N - 1),
                (N - 1, N - 1, 0), (N - 1, N - 1, N - 1)]

    while to_check:
        coord = to_check.pop()
        if new_cube[coord] == 1:
            continue  # rock

        x = coord[1]
        y = coord[0]
        z = coord[2]

        possible_neighbors = [(y + 1, x, z), (y - 1, x, z), (y, x + 1, z),
                              (y, x - 1, z), (y, x, z + 1), (y, x, z - 1)]

        # For each possible neighboring coord, if neighbour is air, fill it
        for p in possible_neighbors:
            if p[0] < 0 or p[1] < 0 or p[2] < 0:
                continue
            elif p[0] >= N or p[1] >= N or p[2] >= N:
                continue
            elif new_cube[p] == 2:
                continue
            elif cube[p] == 0:
                to_check.append(p)
                new_cube[p] = 2

    return new_cube


def get_surface_area_v2(input_file: str, air_cubes: np.ndarray):
    """

    Args:
        input_file:
        air_cubes:

    Returns:

    """
    s_area = 0
    N = air_cubes.shape[0]
    with open(input_file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        x, y, z = line.strip().split(",")
        x = int(x) - 1
        y = int(y) - 1
        z = int(z) - 1

        total_neighbors = 0
        possible_neighbors = [(y + 1, x, z), (y - 1, x, z), (y, x + 1, z),
                              (y, x - 1, z), (y, x, z + 1), (y, x, z - 1)]

        # For each possible neighboring coord, if it doesn't have a neighbor
        # then increase the surface area by 1
        for p in possible_neighbors:
            if p[0] < 0 or p[1] < 0 or p[2] < 0:
                total_neighbors += 1
            elif p[0] >= N or p[1] >= N or p[2] >= N:
                total_neighbors += 1
            elif air_cubes[p] == 2:
                total_neighbors += 1

        s_area += total_neighbors

    return s_area
