from functions_day_16 import *

# # # challenge 1:
# pipes = parse_pipes('../input_files/input_day_16.txt')
# best_pressure, best_path = best_route(pipes, minutes=30)
#
# print("Best path")
# print(best_path)
# print("Best pressure")
# print(best_pressure)

# # challenge 2:
pipes = parse_pipes('../input_files/input_day_16.txt')
best_pressure, best_path = best_route_with_2(pipes, minutes=26)

print("Best path")
print(best_path)
print("Best pressure")
print(best_pressure)
