import pytest

from main_functions import *


@pytest.mark.parametrize("opponent, response",
                         [("A", "Y"),
                          ("B", "Z"),
                          ("C", "X")])
def test_best_reply(opponent, response):
    this_response = rps_best_reply(opponent)
    assert (this_response == response)


@pytest.mark.parametrize("opponent, response",
                         [("A", "Z"),
                          ("B", "X"),
                          ("C", "Y")])
def test_best_reply(opponent, response):
    this_response = rps_worst_reply(opponent)
    assert (this_response == response)


def test_read_strategy_guide():
    df = read_in_rps_strategy_guide('input_files/input_day_2_example.txt')
    pd.testing.assert_frame_equal(df,
                                  pd.DataFrame({'opponent': ["A", "B", "C"], 'response': ['Y', 'X', 'Z']}))


def test_strategy_guide():
    strategy_guide = read_in_rps_strategy_guide('input_files/input_day_2_example.txt')
    score = compute_score_rsp_strategy(strategy_guide)
    assert (score == 15)


def test_strategy_guide_v2():
    strategy_guide = read_in_rps_strategy_guide('input_files/input_day_2_example.txt')
    score = compute_score_rsp_strategy_v2(strategy_guide)
    assert (score == 12)
