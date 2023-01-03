import numpy as np

from functions_day_24 import *

initial_state = parse_cave('../input_files/input_day_24.txt')

#movements = move_in_cave_dijkstra(initial_state)
movements = move_in_cave(initial_state, cap=301)
print(movements)