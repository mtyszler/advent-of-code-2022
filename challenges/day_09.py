from functions_day_09 import *

# challenge 1:
grid_tail = parse_movements('../input_files/input_day_09.txt', grid_size=600)
np.savetxt("grid_v1.txt", grid_tail, fmt='%0i')

print("Locations tail")
print(sum(sum(grid_tail)))

# challenge 2:
grid_tail = parse_movements_v2('../input_files/input_day_09.txt', grid_size=600)
np.savetxt("grid_v2.txt", grid_tail, fmt='%0i')
print("Locations tail")
print(sum(sum(grid_tail)))