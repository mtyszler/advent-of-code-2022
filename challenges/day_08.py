from functions_day_08 import *

# challenge 1:

grid = parse_grid('../input_files/input_day_08.txt')
grid_visibility = visibility_tree(grid)

print("Visible trees")
print(sum(sum(grid_visibility)))

# challenge 2:
grid = parse_grid('../input_files/input_day_08.txt')
grid_scenic_score = scenic_score(grid)

print("Scenic scores trees")
print(grid_scenic_score.max())