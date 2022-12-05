from main_functions import *

# challenge 1:

container = parse_initial_locations('../input_files/input_day_5a.txt')
movements = parse_movements_container('../input_files/input_day_5b.txt')
new_container = move_all_elements_container(container, movements)
result = collect_top_items(new_container)

print('top items')
print(result)

container = parse_initial_locations('../input_files/input_day_5a.txt')
movements = parse_movements_container('../input_files/input_day_5b.txt')
new_container = move_all_elements_container_2(container, movements)
result = collect_top_items(new_container)

print('top items v2')
print(result)