import pandas as pd
import numpy as np


def remove_brackets(input_str: str) -> str:
    """

    Args:
        input_str: '[X]'

    Returns:
        'X'

    """

    if not isinstance(input_str, str):
        return input_str
    part_1 = input_str.split(']')[0]
    part_2 = part_1.split('[')[1]

    return part_2


def parse_initial_locations(input_file: str) -> pd.DataFrame:
    """

    Args:
        input_file:

    Returns:

    """
    df = pd.read_fwf(input_file)
    df = df.applymap(remove_brackets)

    return df


def parse_movements_container(input_file: str) -> list[dict]:
    """

    Args:
        input_file:

    Returns:

    """

    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    movements = []
    for line in lines:
        clean = line.split("move")[1].strip()
        move_amount = clean.split("from")[0]

        move_from_to = clean.split("from")[1]
        move_from, move_to = move_from_to.split("to")

        movements.append(
            dict(move_amount=int(move_amount),
                 move_from=int(move_from),
                 move_to=int(move_to))
        )

    return movements


def move_one_element_container(container: pd.DataFrame, move_from: int, move_to: int) -> pd.DataFrame:
    """

    Args:
        container:
        move_from:
        move_to:

    Returns:

    """

    # from
    for count, element in enumerate(container[str(move_from)]):
        if element is np.nan:
            pass
        else:
            from_pile_item = element
            container[str(move_from)][count] = np.nan
            break

    # to
    for count, element in enumerate(container[str(move_to)]):
        if count == 0 and element is not np.nan:
            # first row is already filled:
            empty_df = pd.DataFrame([[np.nan] * len(container.columns)], columns=container.columns)
            container = empty_df.append(container, ignore_index=True)
            container[str(move_to)][0] = from_pile_item
            break

        elif count == (len(container[str(move_to)]) - 1) and element is np.nan:
            # got to the bottom without anything
            container[str(move_to)][count] = from_pile_item
            break

        elif element is np.nan:
            # next
            pass
        else:
            # found first non nan element
            container[str(move_to)][count - 1] = from_pile_item
            break

    return container


def move_all_elements_container(container: pd.DataFrame, movements: list[dict]) -> pd.DataFrame:
    """

    Args:
        container:
        movements:

    Returns:

    """

    for this_movement in movements:
        for i in range(this_movement['move_amount']):
            container = move_one_element_container(container,
                                                   this_movement['move_from'],
                                                   this_movement['move_to'])

    return container


def collect_top_items(container: pd.DataFrame) -> str:
    """

    Args:
        container:

    Returns:

    """

    top_string = ""
    for this_column in container.columns:
        for count, element in enumerate(container[this_column]):
            if element is np.nan:
                pass
            else:
                top_string += element
                break

    return top_string


def move_chunk_of_element_container(container: pd.DataFrame,
                                    move_from: int, move_to: int, move_amount: int) -> pd.DataFrame:
    """

    Args:
        container:
        move_from:
        move_to:
        move_amount:

    Returns:

    """

    # from
    for count, element in enumerate(container[str(move_from)]):
        if element is np.nan:
            pass
        else:
            from_pile_items = container[str(move_from)][count:count + move_amount].copy()
            container[str(move_from)][count: count + move_amount] = np.nan
            break

    # to
    for count, element in enumerate(container[str(move_to)]):
        if count == 0 and element is not np.nan:
            # first row is already filled:
            empty_df = pd.DataFrame(np.nan, index=range(move_amount),
                                    columns=container.columns)
            container = empty_df.append(container, ignore_index=True)
            container[str(move_to)][0: move_amount] = from_pile_items
            break

        elif count == (len(container[str(move_to)]) - 1) and element is np.nan:
            # got to the bottom without anything
            container[str(move_to)][count - move_amount + 1: count + 1] = from_pile_items
            break

        elif element is np.nan:
            # next
            pass
        else:
            # found first non nan element
            if count - move_amount < 0:
                empty_df = pd.DataFrame(np.nan, index=range(-(count - move_amount)),
                                        columns=container.columns)
                container = empty_df.append(container, ignore_index=True)
                container[str(move_to)][0: move_amount] = from_pile_items
            else:
                container[str(move_to)][count - move_amount: count] = from_pile_items
            break

    return container


def move_all_elements_container_2(container: pd.DataFrame, movements: list[dict]) -> pd.DataFrame:
    """

    Args:
        container:
        movements:

    Returns:

    """

    for this_movement in movements:
        container = move_chunk_of_element_container(container,
                                                    this_movement['move_from'],
                                                    this_movement['move_to'],
                                                    this_movement['move_amount'])

    return container
