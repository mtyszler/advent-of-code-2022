from functions_day_14 import *

# challenge 1:
cave = parse_cave('../input_files/input_day_14.txt')

n_drops, cave_filled = drop_sand(cave)
np.savetxt('cave_filled.txt', cave_filled, fmt='%i')

print("N drops")
print(n_drops)

# challenge 2:
cave = parse_cave('../input_files/input_day_14.txt', size=400)

n_drops, cave_filled = drop_sand_with_floor(cave)
np.savetxt('cave_filled_with_floor.txt', cave_filled, fmt='%i')

print("N drops, with floor")
print(n_drops)