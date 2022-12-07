from main_functions import *
from anytree import RenderTree

# challenge 1:

tree = parse_tree('../input_files/input_day_7.txt')
sizes = list_folder_sizes(tree)
print(RenderTree(tree))
print(sizes)
print(len(sizes))

max_size = find_cum_size(sizes, cut_max=100000)
print("max size")
print(max_size)

# challenge 2
tree = parse_tree('../input_files/input_day_7.txt')
sizes = list_folder_sizes(tree)

min_size = find_min_size(sizes, total_size=70000000, need=30000000)
print("min size")
print(min_size)
