from main_functions import *

# challenge 1:

input_file = open('../input_files/input_day_3.txt', 'r')
lines = input_file.readlines()

tot_priority = 0
for line in lines:
    tot_priority += priority_letter(find_overlap_rucksack(line))

print("Priority score")
print(tot_priority)

# challenge 2:
input_file = open('../input_files/input_day_3.txt', 'r')
lines = input_file.readlines()

tot_priority = 0
count = 0
input_strings = []
for line in lines:
    if count < 3:
        input_strings.append(line.rstrip())
        count += 1
    else:
        tot_priority += priority_letter(find_badges_rucksack(
            input_strings[0], input_strings[1], input_strings[2]))
        count = 0
        input_strings = [line.rstrip(), line.rstrip()]
        count += 1
        # print(tot_priority)

tot_priority += priority_letter(find_badges_rucksack(
    input_strings[0], input_strings[1], input_strings[2]))

print("Priority score badges")
print(tot_priority)
