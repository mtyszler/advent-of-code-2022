from functions_day_12 import *

# challenge 1:
grid_height = parse_height_map('../input_files/input_day_12.txt')
best_distance, best_path = find_top(grid_height)

route_map = make_route(grid_height, best_path)
np.savetxt('route_map.txt', route_map, fmt='%3i')

print("Best distance")
print(best_distance)

# challenge 2:
grid_height = parse_height_map('../input_files/input_day_12.txt')
best_distance_scenic, best_path_scenic = find_top_scenic(grid_height)

route_map_scenic = make_route(grid_height, best_path_scenic)
np.savetxt('route_map_scenic.txt', route_map_scenic, fmt='%3i')

print("Best distance scenic")
print(best_distance_scenic)