import copy

from functions_day_18 import *

# # # challenge 1:
input_file = '../input_files/input_day_18.txt'
cube = parse_cubes(input_file, size=21)
area = get_surface_area(input_file, cube)
air_cubes = find_air_cubes(cube)
print("Surface")
print(area)
print(area-1)  # corner correction

print("exterior surface")
print("Number of air cubes")
n_air_cubes = sum(sum(sum(air_cubes == 0)))
print(n_air_cubes)

print("reachable surface")
new_surface = get_surface_area_v2(input_file, air_cubes)
print(new_surface+6*6-2)  # corner correction
