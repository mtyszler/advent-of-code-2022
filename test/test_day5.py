import pandas as pd
import pytest

from main_functions import *


@pytest.mark.parametrize("input_str, return_str",
                         [("[A]", "A"),
                          ("[XY]", "XY")])
def test_parse_string(input_str, return_str):
    r = remove_brackets(input_str)
    assert (r == return_str)


def test_parse_containers():
    df = parse_initial_locations('input_files/input_day_5a_example.txt')
    assert (df['2'].iloc[1] == 'C')


def test_parse_movement_containers():
    movements = parse_movements_container('input_files/input_day_5b_example.txt')
    assert (movements[1]['move_from'] == 1)
    assert (movements[1]['move_amount'] == 3)


def test_move_one_item():
    container = parse_initial_locations('input_files/input_day_5a_example.txt')
    new_container = move_one_element_container(container, move_from=1, move_to=3)
    assert(new_container['3'][1] == 'N')


def test_move_all_items():
    container = parse_initial_locations('input_files/input_day_5a_example.txt')
    movements = parse_movements_container('input_files/input_day_5b_example.txt')
    new_container = move_all_elements_container(container, movements)

    assert(new_container['3'][2] == 'D')
    assert(new_container['2'][3] == 'M')


def test_top_items():
    container = parse_initial_locations('input_files/input_day_5a_example.txt')
    movements = parse_movements_container('input_files/input_day_5b_example.txt')
    new_container = move_all_elements_container(container, movements)
    result = collect_top_items(new_container)

    assert(result == 'CMZ')


def test_move_chunk_item():
    container = parse_initial_locations('input_files/input_day_5a_example.txt')
    new_container = move_chunk_of_element_container(container, move_from=1, move_to=3, move_amount=1)
    assert(new_container['3'][1] == 'N')


def test_move_chunk_item_2():
    container = parse_initial_locations('input_files/input_day_5a_example.txt')
    new_container = move_chunk_of_element_container(container, move_from=1, move_to=3, move_amount=2)
    assert(new_container['3'][1] == 'Z')


def test_move_all_items2():
    container = parse_initial_locations('input_files/input_day_5a_example.txt')
    movements = parse_movements_container('input_files/input_day_5b_example.txt')
    new_container = move_all_elements_container_2(container, movements)

    assert(new_container['3'][2] == 'Z')
    assert(new_container['2'][3] == 'C')


def test_top_items_2():
    container = parse_initial_locations('input_files/input_day_5a_example.txt')
    movements = parse_movements_container('input_files/input_day_5b_example.txt')
    new_container = move_all_elements_container_2(container, movements)

    result = collect_top_items(new_container)

    assert (result == 'MCD')
