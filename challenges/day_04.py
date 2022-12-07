from functions_day_04 import *

# challenge 1:

input_file = open('../input_files/input_day_04.txt', 'r')
lines = input_file.readlines()

tot_overlaps = 0
for line in lines:
    tot_overlaps += is_contained(line)

print("Contained score")
print(tot_overlaps)

# challenge 2:

input_file = open('../input_files/input_day_04.txt', 'r')
lines = input_file.readlines()

tot_overlaps = 0
for line in lines:
    tot_overlaps += has_overlap(line)

print("Has overlap score")
print(tot_overlaps)
