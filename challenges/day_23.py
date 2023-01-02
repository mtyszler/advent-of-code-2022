import numpy as np

from functions_day_23 import *
initial_state = parse_elephants('../input_files/input_day_23.txt', buffer=100)

after = move_elephants(initial_state, n_moves=10)
print(after)

# find empty spots
left = min([x[1] for x in after])
right = max([x[1] for x in after])
top = min([x[0] for x in after])
bottom = max([x[0] for x in after])

# potential spaces:
potential = (right-left+1)*(bottom-top+1)

empty = potential - len(after)
print(empty)

# part 2
print("part 2")
initial_state = parse_elephants('../input_files/input_day_23.txt', buffer=100)

after = move_elephants(initial_state, n_moves=10000)