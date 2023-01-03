from copy import deepcopy

import numpy as np


def parse_cave(input_file: str) -> dict:
    """

    Args:
        input_file:


    Returns:
      list of coordinates
    """

    initial_state = {}
    with open(input_file, 'r') as f:
        lines = f.readlines()

    y = 0
    for line in lines:
        to_read = line.strip()
        for x in range(len(to_read)):
            if to_read[x] == '#':
                initial_state[(x, y)] = 'muur'
            elif to_read[x] == '.':
                pass
            else:
                initial_state[(x, y)] = [to_read[x]]
        y += 1

    return initial_state


best_known = np.inf


def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


def move_in_cave(initial_state: dict, current_pos: int = None,
                 current_count: int = None,
                 level: int = None,
                 cap: int = None) -> int:
    """

    Args:
        initial_state:
        current_pos
        current_count
        level

    Returns:

    """
    global best_known

    if level is None:
        level = 1
    if level % 100 == 0:
        print("level", level)

    left = min([coord[0] for coord in initial_state.keys()]) + 1
    right = max([coord[0] for coord in initial_state.keys()]) - 1
    top = min([coord[1] for coord in initial_state.keys()]) + 1
    bottom = max([coord[1] for coord in initial_state.keys()]) - 1

    y = 0
    for x in range(max([coord[0] for coord in initial_state.keys()])):
        if (x, y) not in initial_state.keys():
            start = (x, y)

    y = max([coord[1] for coord in initial_state.keys()])
    for x in range(max([coord[0] for coord in initial_state.keys()])):
        if (x, y) not in initial_state.keys():
            target = (x, y)

    if current_pos is None:
        current_pos = start
    current_coord = deepcopy(initial_state)

    if current_count is None:
        count = 0
    else:
        count = current_count

    if cap is None:
        cap = (right - left + 1) * (bottom - top + 1)

    while current_pos != target:
        if count > cap:
            print("level", level, 'cut by cap')
            return cap

        md = manhattan(current_pos, target)
        if count + md >= best_known:
            print("level", level, "worse than best known")
            return best_known

        # update snowflakes:
        new_coord = {}
        for coord, value in current_coord.items():
            if value == 'muur':
                new_coord[coord] = value
            else:
                for flake in value:
                    if flake == '>':
                        dest = (coord[0] + 1, coord[1])
                        if dest in current_coord.keys() and current_coord[dest] == 'muur':
                            dest = (left, coord[1])

                    elif flake == '<':
                        dest = (coord[0] - 1, coord[1])
                        if dest in current_coord.keys() and current_coord[dest] == 'muur':
                            dest = (right, coord[1])

                    elif flake == '^':
                        dest = (coord[0], coord[1] - 1)
                        if dest in current_coord.keys() and current_coord[dest] == 'muur':
                            dest = (coord[0], bottom)

                    elif flake == 'v':
                        dest = (coord[0], coord[1] + 1)
                        if dest in current_coord.keys() and current_coord[dest] == 'muur':
                            dest = (coord[0], top)

                    if dest not in new_coord.keys():
                        new_coord[dest] = []

                    new_coord[dest].append(flake)

        current_coord = deepcopy(new_coord)

        # move:
        neighbours = [(current_pos[0] + 1, current_pos[1]),  # '>'
                      (current_pos[0], current_pos[1] + 1),  # 'v'
                      (current_pos[0] - 1, current_pos[1]),  # '<'
                      (current_pos[0], current_pos[1] - 1),  # '^'
                      current_pos]

        potential = []
        for neighbour in neighbours:
            if (neighbour[0] < 0) or \
                    (neighbour[0] > right + 1) or \
                    (neighbour[1] < 0) or \
                    (neighbour[1] > bottom + 1):
                pass
            elif neighbour not in current_coord.keys():
                potential.append(neighbour)

        if len(potential) == 1:
            current_pos = potential[0]
        else:
            for pot in potential:
                movements = move_in_cave(current_coord, pot, count + 1, level + 1, cap=cap)
                if movements < best_known:
                    print("level", level, "new best known: ", movements)
                    best_known = movements
            print("level", level, "all options considered")
            return best_known

        count += 1

    if current_pos == target:
        final = count if count < best_known else best_known
        print("Solution found:", final)
    return final


def update_snowflakes(current_coord: dict) -> dict:
    """

    Args:
        current_coord:

    Returns:

    """
    left = min([coord[0] for coord in current_coord.keys()]) + 1
    right = max([coord[0] for coord in current_coord.keys()]) - 1
    top = min([coord[1] for coord in current_coord.keys()]) + 1
    bottom = max([coord[1] for coord in current_coord.keys()]) - 1

    # update snowflakes:
    new_coord = {}
    for coord, value in current_coord.items():
        if value == 'muur':
            new_coord[coord] = value
        else:
            for flake in value:
                if flake == '>':
                    dest = (coord[0] + 1, coord[1])
                    if dest in current_coord.keys() and current_coord[dest] == 'muur':
                        dest = (left, coord[1])

                elif flake == '<':
                    dest = (coord[0] - 1, coord[1])
                    if dest in current_coord.keys() and current_coord[dest] == 'muur':
                        dest = (right, coord[1])

                elif flake == '^':
                    dest = (coord[0], coord[1] - 1)
                    if dest in current_coord.keys() and current_coord[dest] == 'muur':
                        dest = (coord[0], bottom)

                elif flake == 'v':
                    dest = (coord[0], coord[1] + 1)
                    if dest in current_coord.keys() and current_coord[dest] == 'muur':
                        dest = (coord[0], top)

                else:
                    raise ValueError('Oh oh')

                if dest not in new_coord.keys():
                    new_coord[dest] = []

                new_coord[dest].append(flake)

    return new_coord


def move_in_cave_dijkstra(initial_state: dict) -> int:
    """

    Args:
        initial_state:

    Returns:

    """

    left = min([coord[0] for coord in initial_state.keys()]) + 1
    right = max([coord[0] for coord in initial_state.keys()]) - 1
    top = min([coord[1] for coord in initial_state.keys()]) + 1
    bottom = max([coord[1] for coord in initial_state.keys()]) - 1

    y = 0
    for x in range(max([coord[0] for coord in initial_state.keys()])):
        if (x, y) not in initial_state.keys():
            start = (x, y)

    y = max([coord[1] for coord in initial_state.keys()])
    for x in range(max([coord[0] for coord in initial_state.keys()])):
        if (x, y) not in initial_state.keys():
            target = (x, y)

    visited_coord = {}
    potential_time = {}

    current_pos = start
    current_time = 0
    current_coord = deepcopy(initial_state)

    while target not in visited_coord.keys():
        if len(visited_coord) % 10 == 0:
            print("Visited: ", len(visited_coord))

        neighbours = [(current_pos[0] + 1, current_pos[1]),  # '>'
                      (current_pos[0], current_pos[1] + 1),  # 'v'
                      (current_pos[0] - 1, current_pos[1]),  # '<'
                      (current_pos[0], current_pos[1] - 1)]  # '^'
                      # current_pos]  # stay

        for neighbour in neighbours:
            if (neighbour[0] < 0) or \
                    (neighbour[0] > right + 1) or \
                    (neighbour[1] < 0) or \
                    (neighbour[1] > bottom + 1):
                continue
            elif neighbour in initial_state and initial_state[neighbour] =='muur':
                continue
            elif neighbour in visited_coord:
                pass
            else:
                free_to_move = False
                this_minutes = current_time
                updated_coord = deepcopy(current_coord)

                while not free_to_move:
                    updated_coord = deepcopy(update_snowflakes(updated_coord))
                    this_minutes += 1
                    if neighbour not in updated_coord.keys():
                        free_to_move = True
                    elif current_pos in updated_coord.keys():
                        temp_potential = []
                        for temp_neighbour in neighbours:
                            if (temp_neighbour[0] < 0) or \
                                    (temp_neighbour[0] > right + 1) or \
                                    (temp_neighbour[1] < 0) or \
                                    (temp_neighbour[1] > bottom + 1):
                                continue
                            elif temp_neighbour not in updated_coord.keys():
                                temp_potential.append(temp_neighbour)
                        print(temp_potential)



                if free_to_move and neighbour in potential_time.keys():
                    if this_minutes < potential_time[neighbour][0]:
                        potential_time[neighbour] = (this_minutes, deepcopy(updated_coord))
                elif free_to_move:
                    potential_time[neighbour] = (this_minutes, deepcopy(updated_coord))

        visited_coord[current_pos] = (current_time, deepcopy(current_coord))

        best_time = np.inf
        for coord, minutes in potential_time.items():
            if minutes[0] < best_time:
                best_time = minutes[0]
                best_state = deepcopy(minutes[1])
                best_coord = deepcopy(coord)

        if len(potential_time) > 0:
            del potential_time[best_coord]

        current_pos = deepcopy(best_coord)
        current_time = best_time
        current_coord = deepcopy(best_state)

    return visited_coord[target][0]
