import pandas as pd
import pytest

from main_functions import *


def test_import():
    elves_example = parse_input('input_files/input_day_1_example.txt')
    assert(elves_example['elf_3']['food'] == {'food_1': '5000', 'food_2': '6000'})
    assert(elves_example['elf_2']['total_calories'] == 4000)


def test_max():
    elves_example = parse_input('input_files/input_day_1_example.txt')
    max_elf, max_elf_calories = find_max_calories_elf(elves_example)

    assert (max_elf == 'elf_4')
    assert (max_elf_calories == 24000)


def test_ranked():
    elves_example = parse_input('input_files/input_day_1_example.txt')
    df_elves = ranked_calories_elf(elves_example)
    print(df_elves)
    assert (df_elves.iloc[1, ].name == 'elf_3')
    assert (df_elves.iloc[1, ].calories == 11000)


@pytest.mark.parametrize("opponent, response",
                         [("A", "Y"),
                          ("B", "Z"),
                          ("C", "X")])
def test_best_reply(opponent, response):
    this_response = rps_best_reply(opponent)
    assert(this_response == response)


@pytest.mark.parametrize("opponent, response",
                         [("A", "Z"),
                          ("B", "X"),
                          ("C", "Y")])
def test_best_reply(opponent, response):
    this_response = rps_worst_reply(opponent)
    assert(this_response == response)


def test_read_strategy_guide():

    df = read_in_rps_strategy_guide('input_files/input_day_2_example.txt')
    pd.testing.assert_frame_equal(df,
                                  pd.DataFrame({'opponent': ["A", "B", "C"], 'response': ['Y' , 'X' ,  'Z']}))


def test_strategy_guide():
    strategy_guide = read_in_rps_strategy_guide('input_files/input_day_2_example.txt')
    score = compute_score_rsp_strategy(strategy_guide)
    assert(score == 15)

def test_strategy_guide_v2():
    strategy_guide = read_in_rps_strategy_guide('input_files/input_day_2_example.txt')
    score = compute_score_rsp_strategy_v2(strategy_guide)
    assert (score == 12)
