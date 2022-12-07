import pytest

from main_functions import *
from anytree import RenderTree


def test_parse_tree():
    tree = parse_tree('../input_files/input_day_7_example.txt')
    print(RenderTree(tree))


def test_find_max_size():
    tree = parse_tree('../input_files/input_day_7_example.txt')
    sizes = list_folder_sizes(tree)

    max_size = find_cum_size(sizes, cut_max=100000)

    assert (max_size == 95437)


def test_find_min_delete():
    tree = parse_tree('../input_files/input_day_7_example.txt')
    sizes = list_folder_sizes(tree)

    min_size = find_min_size(sizes, total_size=70000000, need=30000000)

    assert (min_size == 24933642)