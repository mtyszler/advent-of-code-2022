import pytest

from functions_day_11 import *


def test_parse_instructions():
    monkeys, min_common_multiplier = parse_starting_positions('input_files/input_day_11_example.txt')

    assert (monkeys[0]['items'] == [79, 98])
    assert (monkeys[2]['test'] == 13)
    assert (monkeys[3]['false'] == 1)


def test_single_round():
    monkeys, min_common_multiplier = parse_starting_positions('input_files/input_day_11_example.txt')
    monkeys = run_monkeys(monkeys, n_rounds=1, min_common_multiplier=min_common_multiplier)
    items = [monkeys['items'] for monkeys in monkeys]
    print("")
    print(items)

    assert (items[0] == [20, 23, 27, 26])
    assert (items[3] == [])


def test_monkey_business():
    monkeys, min_common_multiplier = parse_starting_positions('input_files/input_day_11_example.txt')
    monkeys = run_monkeys(monkeys, n_rounds=20, min_common_multiplier=min_common_multiplier)

    value_monkey_business = monkey_business(monkeys)

    assert (value_monkey_business == 10605)


def test_monkey_business_v2():
    monkeys, min_common_multiplier = parse_starting_positions('input_files/input_day_11_example.txt')
    monkeys = run_monkeys(monkeys, n_rounds=10000, relief=1, min_common_multiplier=min_common_multiplier)

    value_monkey_business = monkey_business(monkeys)

    assert (value_monkey_business == 2713310158)
