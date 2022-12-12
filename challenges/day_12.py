from functions_day_12 import *

# challenge 1:
grid_height = parse_height_map('../input_files/input_day_12.txt')
top_steps, tracking_grid = find_top_v1(grid_height)

print("N steps")
print(top_steps)