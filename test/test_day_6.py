import pytest

from main_functions import *


@pytest.mark.parametrize("input_str, return_pos",
                         [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
                          ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
                          ("nppdvjthqldpwncqszvftbrmjlhg", 6),
                          ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
                          ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)])
def test_find_signal(input_str, return_pos):
    signal_pos, signal_str = find_starter_of_marker(input_str,
                                                    signal_length=4, occurrence=1)
    print(signal_str)
    print(signal_pos)
    assert (signal_pos == return_pos)

@pytest.mark.parametrize("input_str, return_pos",
                         [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
                          ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
                          ("nppdvjthqldpwncqszvftbrmjlhg", 23),
                          ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
                          ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)])
def test_find_signal_long(input_str, return_pos):
    signal_pos, signal_str = find_starter_of_marker(input_str,
                                                    signal_length=14, occurrence=1)
    print(signal_str)
    print(signal_pos)
    assert (signal_pos == return_pos)
