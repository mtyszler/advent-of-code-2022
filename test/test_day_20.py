import numpy as np
import pytest

from functions_day_20 import *


def test_decoder():
    decoded = decode('input_files/input_day_20_example.txt')

    after = [None] * len(decoded)
    for item in decoded:
        after[item['current_index']]=item['value']

    print(decoded)
    print("")
    print(after)

    zero_index = np.argwhere(np.array(after) == 0)[0][0]
    pos = 1000 + zero_index
    index = ((pos + 1) % len(decoded)) - 1
    p1 = after[index]
    pos = 2000 + zero_index
    index = ((pos + 1) % len(decoded)) - 1
    p2 = after[index]
    pos = 3000 + zero_index
    index = ((pos + 1) % len(decoded)) - 1
    p3 = after[index]

    print(p1, p2, p3)
    s = p1 + p2 + p3
    print(s)


