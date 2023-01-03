from copy import deepcopy

import numpy as np


def snafu_to_decimal(input_file: str = None, string: str = None) -> list:
    """

    Args:
        input_file:
        string


    Returns:
      list of coordinates
    """

    converted = []

    if input_file is not None:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            snafu = line.strip()
            converted.append(convert_from_snafu(snafu))

    else:
        converted.append(convert_from_snafu(string))

    return converted


def convert_from_snafu(string: str) -> int:
    """

    Args:
        string:

    Returns:

    """

    number = 0
    for i in range(len(string)):
        this_string = string[-(i + 1)]
        if this_string == '=':
            this_string = -2
        elif this_string == '-':
            this_string = -1
        else:
            this_string = int(this_string)

        number += this_string * (5 ** i)

    return number


def convert_to_snafu(number: int) -> int:
    """

    Args:
        number:

    Returns:

    """

    list_ = []

    while number > 0:

        rest = number % 5
        number = number // 5

        if rest < 3:
            this_rest = str(rest)

        elif rest == 3:

            this_rest = "="
            number += 1

        elif rest == 4:
            this_rest = "-"
            number += 1

        list_.insert(0, this_rest)

    return ''.join([str(part) for part in list_])
