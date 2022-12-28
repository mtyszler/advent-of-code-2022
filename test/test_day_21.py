import numpy as np
import pytest

from functions_day_21 import *


def test_decoder():
    monkeys = decode('input_files/input_day_21_example.txt')

    print("")
    print(monkeys)
    print('root')
    print(monkeys['root'])
    assert (monkeys['root'] == 152)


def test_decoder_v2():
    monkeys = decode_v2('input_files/input_day_21_example.txt')

    print("")
    print(monkeys)
    print('root')
    print(monkeys['humn'])
    assert (monkeys['humn'] == 301)
