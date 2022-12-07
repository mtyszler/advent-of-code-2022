import pytest

from main_functions import *


@pytest.mark.parametrize("input_str, overlapped",
                         [("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
                          ("PmmdzqPrVvPwwTWBwg", "P"),
                          ("ttgJtRGJQctTZtZT", "t")])
def test_split_find(input_str, overlapped):
    overlapped_function = find_overlap_rucksack(input_str)

    assert (overlapped == overlapped_function)


@pytest.mark.parametrize("input_str, points",
                         [("a", 1),
                          ("z", 26),
                          ("Z", 52)])
def test_letter_converter(input_str, points):
    points_function = priority_letter(input_str)

    assert (points == points_function)


def test_example():
    input_file = open('input_files/input_day_3_example.txt', 'r')
    lines = input_file.readlines()

    tot_priority = 0
    for line in lines:
        tot_priority += priority_letter(find_overlap_rucksack(line))

    assert (tot_priority == 157)


def test_example2():
    input_file = open('input_files/input_day_3_example.txt', 'r')
    lines = input_file.readlines()

    tot_priority = 0
    count = 0
    input_strings = []
    for line in lines:
        if count < 3:
            input_strings.append(line.rstrip())
            count += 1
        else:
            tot_priority += priority_letter(find_badges_rucksack(
                input_strings[0], input_strings[1], input_strings[2]))
            count = 0
            input_strings = [line]
            count += 1

    tot_priority += priority_letter(find_badges_rucksack(
        input_strings[0], input_strings[1], input_strings[2]))

    assert (tot_priority == 70)
