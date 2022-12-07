import pandas as pd


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
