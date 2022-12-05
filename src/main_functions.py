import pandas as pd
import numpy as np
import difflib


# Day 1


def parse_input(filename: str) -> dict:
    """
     convert input file into a dictionary of dictionaries on elves food

    Args:
        filename: txt file if input of elves food
    :return:
        output format:
        elves = {
            food = {
                'food_1': xxx,
                ...


            }
            total_calories: yyy
    """

    input_file = open(filename, 'r')
    lines = input_file.readlines()

    # initialize
    elves = {}
    count_elves = 1
    elves['elf_' + str(count_elves)] = {}
    elves['elf_' + str(count_elves)]['food'] = {}
    count_food = 1
    cum_tot = 0

    for line in lines:

        if line.strip():
            # 'The line is NOT empty
            elves['elf_' + str(count_elves)]['food']['food_' + str(count_food)] = line.strip()
            cum_tot += int(line.strip())
            count_food += 1
        else:
            # The line is empty'
            elves['elf_' + str(count_elves)]['total_calories'] = cum_tot

            # reset
            count_elves += 1
            elves['elf_' + str(count_elves)] = {}
            elves['elf_' + str(count_elves)]['food'] = {}
            count_food = 1
            cum_tot = 0

        if line.strip():
            # The last line is no empty
            elves['elf_' + str(count_elves)]['total_calories'] = cum_tot

    return elves


def find_max_calories_elf(elves: dict) -> [str, int]:
    """
    Find max calories elf

    Args:
         elves: see parse_input
    :return:
        max_calories, max(total_calories.values())
    """
    total_calories = {elf: values['total_calories'] for elf, values in elves.items()}
    max_calories = [key for key, value in total_calories.items() if value == max(total_calories.values())]

    return max_calories[0], max(total_calories.values())


def ranked_calories_elf(elves: dict) -> pd.DataFrame:
    """
    Compute ranked table of elves

    Args:
        elves: see parse_input
    Returns:

        max_calories, max(total_calories.values())
    """

    total_calories = {elf: values['total_calories'] for elf, values in elves.items()}
    df_elves = pd.DataFrame.from_dict(total_calories, orient='index', columns=['calories']).sort_values(by='calories',
                                                                                                        ascending=False)

    return df_elves


# Day 2

def rps_best_reply(opponent: str) -> str:
    """
    Best reply to Rock Paper Scissors

    Rock (A) ==> beaten by Paper (Y)
    Paper (B) ==> beaten by Scissors (Z)
    Scissors (C) ==> beaten by Rock (X)

    Args:
        opponent: play of opponent
    Returns:
        response to win
    """

    if opponent == "A":
        response = "Y"
    elif opponent == "B":
        response = "Z"
    elif opponent == "C":
        response = "X"
    else:
        raise ValueError("Please input 'A', 'B', or 'C'")

    return response


def rps_worst_reply(opponent: str) -> str:
    """
    Worst reply to Rock Paper Scissors

    Rock (A) ==> beats Scissors (Z)
    Paper (B) ==> beats Rock (X)
    Scissors (C) ==> beats Paper (Y)

    Args:
        opponent: play of opponent
    Returns:
        response to win
    """

    if opponent == "A":
        response = "Z"
    elif opponent == "B":
        response = "X"
    elif opponent == "C":
        response = "Y"
    else:
        raise ValueError("Please input 'A', 'B', or 'C'")

    return response


def read_in_rps_strategy_guide(filename: str) -> pd.DataFrame:
    """
    Args:
        filename
    Returns:
        dataframe with opponent, response
    """

    df = pd.read_table(filename, delimiter=" ", names=['opponent', 'response'])

    return df


def _compute_rps_play_score(opponent: str, response: str) -> int:
    """
    Compute scores of a Rock, Scissors, Paper strategy game

    Rock (A) ==> beaten by Paper (Y), play score = 2
    Paper (B) ==> beaten by Scissors (Z), play score = 3
    Scissors (C) ==> beaten by Rock (X), play score = 1

    Outcome score:
    Loss = 0
    Draw = 3
    Win = 6

    Args:
        opponent: A, B or C
        response (play): X, Y or Z
    Returns:
        play score
    """

    # response score
    if response == "Y":
        play_score = 2
    elif response == "Z":
        play_score = 3
    elif response == "X":
        play_score = 1
    else:
        raise ValueError("Please input 'X', 'Y', or 'Z' as response")

    if opponent not in ['A', 'B', 'C']:
        raise ValueError("Please input 'A', 'B', or 'C' for opponent")

    # outcome score:
    equivalency = dict(X="A", Y="B", Z="C")

    if opponent == equivalency[response]:
        # tie:
        outcome_score = 3
    elif response == rps_best_reply(opponent):
        # win:
        outcome_score = 6
    else:  # opponent == best response (response):
        # loss:
        outcome_score = 0

    return play_score + outcome_score


def compute_score_rsp_strategy(strategy_guide: pd.DataFrame) -> int:
    """
    Compute scores of a Rock, Scissors, Paper strategy guide

    Rock (A) ==> beaten by Paper (Y), play score = 2
    Paper (B) ==> beaten by Scissors (X), play score = 3
    Scissors (C) ==> beaten by Rock (Z), play score = 1

    Outcome score:
    Loss = 0
    Draw = 3
    Win = 6


    Args:
        strategy_guide: dataframe with input and response
    Returns:
        set score
    """

    # get best response
    strategy_guide['game score'] = strategy_guide.apply(lambda row:
                                                        _compute_rps_play_score(row['opponent'], row['response']),
                                                        axis=1)

    return sum(strategy_guide['game score'])


def _compute_rps_play_score_v2(opponent: str, response: str) -> int:
    """
    Compute scores of a Rock, Scissors, Paper strategy game

    Rock (A) ==> beaten by Paper (Y), play score = 2
    Paper (B) ==> beaten by Scissors (X), play score = 3
    Scissors (C) ==> beaten by Rock (Z), play score = 1

    Outcome score:
    Loss = 0
    Draw = 3
    Win = 6

    X means you need to lose
    Y means you need to draw
    Z means you need to win

    Args:
        opponent: A, B or C
        response (strategy): X, Y or Z
    Returns:
        play score
    """

    equivalency = dict(A="X", B="Y", C="Z")
    # response score
    if response == "Y":
        outcome_score = 3
        play = equivalency[opponent]
    elif response == "Z":
        outcome_score = 6
        play = rps_best_reply(opponent)
    elif response == "X":
        outcome_score = 0
        play = rps_worst_reply(opponent)
    else:
        raise ValueError("Please input 'X', 'Y', or 'Z' as response")

    if opponent not in ['A', 'B', 'C']:
        raise ValueError("Please input 'A', 'B', or 'C' for opponent")

    # response score
    if play == "Y":
        play_score = 2
    elif play == "Z":
        play_score = 3
    elif play == "X":
        play_score = 1
    else:
        raise ValueError("Please input 'X', 'Y', or 'Z' as play")

    return play_score + outcome_score


def compute_score_rsp_strategy_v2(strategy_guide: pd.DataFrame) -> int:
    """
    Compute scores of a Rock, Scissors, Paper strategy guide

    Rock (A) ==> beaten by Paper, play score = 2
    Paper (B) ==> beaten by Scissors  play score = 3
    Scissors (C) ==> beaten by Rock, play score = 1

    Outcome score:
    Loss = 0
    Draw = 3
    Win = 6

    X means you need to lose
    Y means you need to draw
    Z means you need to win

    Args:
        strategy_guide: dataframe with input and response
    Returns:
        set score
    """

    # get best response
    strategy_guide['game score'] = strategy_guide.apply(lambda row:
                                                        _compute_rps_play_score_v2(row['opponent'], row['response']),
                                                        axis=1)

    return sum(strategy_guide['game score'])


# day 3

def find_overlap_rucksack(input_str: str) -> str:
    """
    split string in 2 and find overlap

    Args:
        input_str:

    Returns:
        overlapping str

    """

    N = len(input_str)
    part_1 = input_str[0:int(N / 2)]
    part_2 = input_str[int(N / 2):]

    s = difflib.SequenceMatcher(None, part_1, part_2)
    pos_a, pos_b, size = s.find_longest_match(0, len(part_1), 0, len(part_2))
    return part_1[pos_a:pos_a + size]


def priority_letter(letter: str) -> int:
    """
    a-z: 1 to 26
    A-Z: 27 to 52

    Args:
        letter:

    Returns:
        letter to int
    """

    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26


def find_badges_rucksack(input_str_1: str, input_str_2: str, input_str_3: str) -> str:
    """
   find common letter in 3 strings

    Args:
        input_str_1:
        input_str_2:
        input_str_3:

    Returns:
        overlapping str

    """

    overlap = set(input_str_1) & set(input_str_2) & set(input_str_3)
    # print(overlap)

    return list(overlap)[0]


# Day 4


def make_one_range(input_str: str) -> range:
    """

    Args:
        input_str: X-Y

    Returns:
        range(X, Y+1)

    """
    start, end = input_str.split(sep="-")

    return range(int(start), int(end) + 1)


def make_ranges(input_str: str) -> [range, range]:
    """

    Args:
        input_str: X-Y, Z-W

    Returns:
        range_1 (X, Y+1), range_2(Z-W+1)

    """

    chunk_1, chunk_2 = input_str.split(sep=',')

    return make_one_range(chunk_1), make_one_range(chunk_2)


def is_contained(input_str: str) -> bool:
    """

    Args:
        input_str: X-Y, Z-W

    Returns:
        True if range1 within range2 or vice-versa
    """

    range_1, range_2 = make_ranges(input_str)

    overlap = set(range_1) & set(range_2)
    if overlap == set(range_1) or overlap == set(range_2):
        return True
    else:
        return False


def has_overlap(input_str: str) -> bool:
    """

    Args:
        input_str: X-Y, Z-W

    Returns:
        True if range1 overlaps range2
    """

    range_1, range_2 = make_ranges(input_str)

    overlap = set(range_1) & set(range_2)
    if overlap == set():
        return False
    else:
        return True


# Day 5


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
