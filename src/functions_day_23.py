from copy import deepcopy
from itertools import chain

import numpy as np


def parse_elephants(input_file: str, buffer: int) -> list:
    """

    Args:
        input_file:
        buffer

    Returns:
      list of coordinates of elephants
    """

    initial_state = []
    with open(input_file, 'r') as f:
        lines = f.readlines()

    row = 0
    for line in lines:
        to_read = line.strip()
        for col in range(len(to_read)):
            if to_read[col] == '#':
                initial_state.append((row + buffer, col + buffer))
        row += 1

    return initial_state


def move_elephants(initial_state: list, n_moves: int) -> list:
    """

    Args:
        initial_state:
        n_moves:

    Returns:

    """
    movements = ['north', 'south', 'west', 'east']
    current_position = deepcopy(initial_state)

    for jj in range(n_moves):
        old_position = [x for x in current_position]
        destination = {}

        # proposed positions
        for elephant in current_position:
            neighbours = [(elephant[0] - 1, elephant[1] - 1),  # 0 NW
                          (elephant[0] - 1, elephant[1]),  # 1 N
                          (elephant[0] - 1, elephant[1] + 1),  # 2 NE
                          (elephant[0], elephant[1] + 1),  # 3 E
                          (elephant[0] + 1, elephant[1] + 1),  # 4 SE
                          (elephant[0] + 1, elephant[1]),  # 5 S
                          (elephant[0] + 1, elephant[1] - 1),  # 6 SW
                          (elephant[0], elephant[1] - 1)]  # 7 W

            # check surroundings:
            elephant_next_to_it = False
            for neighbour in neighbours:
                if neighbour in current_position:
                    elephant_next_to_it = True
                    break

            # if busy, move
            if elephant_next_to_it:
                for pos in movements:
                    if pos == 'north':
                        to_check = neighbours[0:3]
                    elif pos == 'south':
                        to_check = neighbours[4:7]
                    elif pos == 'east':
                        to_check = neighbours[2:5]
                    elif pos == 'west':
                        to_check = [*neighbours[6:8], neighbours[0]]

                    found_empty = True
                    for cell in to_check:
                        if cell in current_position:
                            found_empty = False
                            break

                    if found_empty:
                        if pos == 'north':
                            destination[elephant] = neighbours[1]
                        elif pos == 'south':
                            destination[elephant] = neighbours[5]
                        elif pos == 'west':
                            destination[elephant] = neighbours[7]
                        elif pos == 'east':
                            destination[elephant] = neighbours[3]

                        break

        # complete destinations:
        for original in current_position:
            if original not in destination.keys():
                destination[original] = original

        # check conflicts:
        # finding duplicate values
        # from dictionary using set
        rev_destination = {}
        for key, value in destination.items():
            rev_destination.setdefault(value, set()).add(key)

        conflicts = set(chain.from_iterable(
            values for key, values in rev_destination.items()
            if len(values) > 1))

        for conflict in conflicts:
            destination[conflict] = conflict

        # update order:
        first_mov = movements.pop(0)
        movements.append(first_mov)

        # update current_position:
        current_position = destination.values()

        left = min([x[1] for x in current_position])
        right = max([x[1] for x in current_position])
        top = min([x[0] for x in current_position])
        bottom = max([x[0] for x in current_position])

        print("round", jj)
        if set(old_position) == set(current_position):
            print("done")
            break

    return current_position
