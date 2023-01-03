import numpy as np
import pytest

from functions_day_25 import *


@pytest.mark.parametrize("decoded, snafu",
                         [("1", "1"),
                          ("2", "2"),
                          ("3", "1="),
                          ("4", "1-"),
                          ("5", "10"),
                          ("6", "11"),
                          ("7", "12"),
                          ("8", "2="),
                          ("9", "2-"),
                          ("10", "20"),
                          ("15", "1=0"),
                          ("20", "1-0"),
                          ("2022", "1=11-2"),
                          ("12345", "1-0---0"),
                          ("314159265", "1121-1110-1=0")])
def test_decoder_v0(decoded, snafu):
    this_decoded = snafu_to_decimal(string=snafu)

    assert (str(this_decoded[0]) == decoded)


def test_decoder():
    decoded = snafu_to_decimal(input_file='input_files/input_day_25_example.txt')

    assert (sum(decoded) == 4890)
    assert (convert_to_snafu(sum(decoded)) == '2=-1=0')


@pytest.mark.parametrize("decimal, snafu",
                         [("1", "1"),
                          ("2", "2"),
                          ("3", "1="),
                          ("4", "1-"),
                          ("5", "10"),
                          ("6", "11"),
                          ("7", "12"),
                          ("8", "2="),
                          ("9", "2-"),
                          ("10", "20"),
                          ("15", "1=0"),
                          ("20", "1-0"),
                          ("2022", "1=11-2"),
                          ("12345", "1-0---0"),
                          ("314159265", "1121-1110-1=0")])
def test_decoder_v1(decimal, snafu):
    this_encoded = convert_to_snafu(int(decimal))

    assert (this_encoded == snafu)
