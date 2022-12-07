import pytest

from main_functions import *


@pytest.mark.parametrize("input_str, overlapped",
                         [("2-4,6-8", False),
                          ("2-8,3-7", True),
                          ("6-6,4-6", True)])
def test_contained(input_str, overlapped):
    overlapped_function = is_contained(input_str)

    assert (overlapped == overlapped_function)


@pytest.mark.parametrize("input_str, overlapped",
                         [("2-4,6-8", False),
                          ("2-8,3-7", True),
                          ("6-6,4-6", True),
                          ("2-4,4-6", True)])
def test_contained(input_str, overlapped):
    overlapped_function = has_overlap(input_str)

    assert (overlapped == overlapped_function)


@pytest.mark.parametrize("input_str, res_range",
                         [("2-4", range(2, 5)),
                          ("6-6", range(6, 7))])
def test_single_range(input_str, res_range):
    range_function = make_one_range(input_str)

    assert (range_function == res_range)


@pytest.mark.parametrize("input_str, res_range",
                         [("2-4,4-6", [range(2, 5), range(4, 7)]),
                          ("6-6,6-9", [range(6, 7), range(6, 10)])])
def test_single_range(input_str, res_range):
    range_1, range_2 = make_ranges(input_str)

    assert ([range_1, range_2] == res_range)


def test_example():
    input_file = open('input_files/input_day_4_example.txt', 'r')
    lines = input_file.readlines()

    tot_overlaps = 0
    for line in lines:
        tot_overlaps += is_contained(line)

    assert (tot_overlaps == 2)


def test_example2():
    input_file = open('input_files/input_day_4_example.txt', 'r')
    lines = input_file.readlines()

    tot_overlaps = 0
    for line in lines:
        tot_overlaps += has_overlap(line)

    assert (tot_overlaps == 4)
