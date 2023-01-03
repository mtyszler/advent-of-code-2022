import numpy as np

from functions_day_25 import *

decoded = snafu_to_decimal(input_file='../input_files/input_day_25.txt')

print(convert_to_snafu(sum(decoded)))