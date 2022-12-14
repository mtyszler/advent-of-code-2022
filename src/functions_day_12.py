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


def find_top(grid_height: np.ndarray) -> [int, list]:
    """
    Dijkstra algorithm

    Args:
        grid_height:

    Returns:

    """

    # initialize supporting matrices
    unvisited = np.ones_like(grid_height, dtype='float')
    distances = np.ones_like(grid_height, dtype='i') * np.inf
    best_path = np.empty_like(grid_height, dtype=object)

    # relevant start and target:
    start_location = np.argwhere(grid_height == 'S')
    start_row = start_location[0][0]
    start_col = start_location[0][1]

    target_location = np.argwhere(grid_height == 'E')
    target_row = target_location[0][0]
    target_col = target_location[0][1]

    # initialize search:
    unvisited[start_row, start_col] = np.nan
    distances[start_row, start_col] = 0
    best_path[start_row, start_col] = [[start_row, start_col]]

    internal_counter = 0
    while unvisited[target_row, target_col] == 1:  # keep going until top is found
        internal_counter += 1
        if np.mod(internal_counter, 1000) == 0:
            print("current iteration: ", internal_counter)

        # check for potential improvements on every node reachable by the current visited nodes
        for node in np.argwhere(np.isnan(unvisited)):
            current_row = node[0]
            current_col = node[1]

            # assess neighbours:
            current_letter = grid_height[current_row, current_col]
            current_value = 1 if current_letter == "S" else ord(current_letter) - 96

            for neighbor_row, neighbor_col in [[current_row, current_col + 1],
                                               [current_row + 1, current_col],
                                               [current_row, current_col - 1],
                                               [current_row - 1, current_col]]:

                # check for edges
                if neighbor_row < 0 or neighbor_col < 0 or \
                        neighbor_row >= grid_height.shape[0] or neighbor_col >= grid_height.shape[1]:
                    continue

                # skip visited nodes:
                if np.isnan(unvisited[neighbor_row, neighbor_col]):
                    continue

                next_letter = grid_height[neighbor_row, neighbor_col]
                diff_level = _eval_letter(current_value, next_letter)

                if diff_level <= 1:  # reachable
                    potential_distance = distances[current_row, current_col] + 1
                    if potential_distance < distances[neighbor_row, neighbor_col]:  # found an improvement
                        # save distance
                        distances[neighbor_row, neighbor_col] = potential_distance

                        # save path
                        current_path = best_path[current_row, current_col].copy()
                        current_path.append([neighbor_row, neighbor_col])
                        best_path[neighbor_row, neighbor_col] = current_path.copy()

        # find the closest node among the unvisited nodes:
        unvisited_distances = np.multiply(unvisited, distances)
        closest_nodes = np.argwhere(unvisited_distances == np.nanmin(unvisited_distances))
        # break ties:
        best_distance_to_top = np.inf
        for i in range(len(closest_nodes)):
            this_node_row = closest_nodes[i][0]
            this_node_col = closest_nodes[i][1]
            distance_to_top = np.sqrt((target_col - this_node_row) ** 2 + (target_row - this_node_col) ** 2)
            if distance_to_top < best_distance_to_top:
                best_distance_to_top = distance_to_top
                best_node = closest_nodes[i]

        # mark the closest node as visited
        unvisited[best_node[0], best_node[1]] = np.nan

    return distances[target_row, target_col], best_path[target_row, target_col]


def make_route(grid_height: np.ndarray, path: list) -> np.ndarray:
    """

    Args:
        grid_height:
        path:

    Returns:

    """

    route_map = np.zeros_like(grid_height, dtype='i')
    step = 1
    for node in path:
        route_map[node[0], node[1]] = step
        step += 1

    return route_map


def _eval_letter(current_value: int, next_letter: str) -> int:
    """

    Args:
        current_value:
        next_letter:

    Returns:
         diff level between current letter and next letter

    """

    if next_letter == "E":
        next_value_diff = ord('z') - 96 - current_value
    elif next_letter == "S":
        next_value_diff = ord('a') - 96 - current_value
    else:
        next_value_diff = ord(next_letter) - 96 - current_value

    return next_value_diff


def find_top_scenic(grid_height: np.ndarray) -> [int, list]:
    """
    Dijkstra algorithm

    Args:
        grid_height:

    Returns:

    """

    # initialize supporting matrices
    unvisited = np.ones_like(grid_height, dtype='float')
    distances = np.ones_like(grid_height, dtype='i') * np.inf
    best_path = np.empty_like(grid_height, dtype=object)

    # relevant start and target:
    start_location = np.argwhere(grid_height == 'E')
    start_row = start_location[0][0]
    start_col = start_location[0][1]

    # initialize search:
    unvisited[start_row, start_col] = np.nan
    distances[start_row, start_col] = 0
    best_path[start_row, start_col] = [[start_row, start_col]]

    internal_counter = 0
    n_unvisited_old = 0
    while (n_unvisited_old != np.nansum(unvisited)) and (np.nansum(unvisited) != 0):  # keep going until all routes are traced
        n_unvisited_old = np.nansum(unvisited)
        internal_counter += 1
        if np.mod(internal_counter, 1000) == 0:
            print("current iteration: ", internal_counter)

        # check for potential improvements on every node reachable by the current visited nodes
        for node in np.argwhere(np.isnan(unvisited)):
            current_row = node[0]
            current_col = node[1]

            # assess neighbours:
            current_letter = grid_height[current_row, current_col]
            current_value = 1 if current_letter == "S" else ord(current_letter) - 96

            for neighbor_row, neighbor_col in [[current_row, current_col + 1],
                                               [current_row + 1, current_col],
                                               [current_row, current_col - 1],
                                               [current_row - 1, current_col]]:

                # check for edges
                if neighbor_row < 0 or neighbor_col < 0 or \
                        neighbor_row >= grid_height.shape[0] or neighbor_col >= grid_height.shape[1]:
                    continue

                # skip visited nodes:
                if np.isnan(unvisited[neighbor_row, neighbor_col]):
                    continue

                next_letter = grid_height[neighbor_row, neighbor_col]
                diff_level = _eval_letter(current_value, next_letter) * -1  # invert because we're looking backwards

                if diff_level <= 1:  # reachable
                    potential_distance = distances[current_row, current_col] + 1
                    if potential_distance < distances[neighbor_row, neighbor_col]:  # found an improvement
                        # save distance
                        distances[neighbor_row, neighbor_col] = potential_distance

                        # save path
                        current_path = best_path[current_row, current_col].copy()
                        current_path.append([neighbor_row, neighbor_col])
                        best_path[neighbor_row, neighbor_col] = current_path.copy()

        # find the closest node among the unvisited nodes:
        unvisited_distances = np.multiply(unvisited, distances)
        closest_nodes = np.argwhere(unvisited_distances == np.nanmin(unvisited_distances))
        # break ties, take the first one:
        best_node = closest_nodes[0]

        # mark the closest node as visited
        unvisited[best_node[0], best_node[1]] = np.nan

    # find the best a-E route:
    nodes_a = np.argwhere(grid_height == 'a')

    # initialize to 'S'
    best_node = np.argwhere(grid_height == 'S')
    this_node_row = best_node[0][0]
    this_node_col = best_node[0][1]
    best_distance_to_top = distances[this_node_row, this_node_col]

    for i in range(len(nodes_a)):
        this_node_row = nodes_a[i][0]
        this_node_col = nodes_a[i][1]
        distance_to_top = distances[this_node_row, this_node_col]
        if distance_to_top < best_distance_to_top:
            best_distance_to_top = distance_to_top
            best_node = nodes_a[i]

    return distances[best_node[0], best_node[1]], best_path[best_node[0], best_node[1]]
