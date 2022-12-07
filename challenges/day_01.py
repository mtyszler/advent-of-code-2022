from functions_day_01 import *

# challenge 1
elves = parse_input('../input_files/input_day_01.txt')
max_elf, max_elf_calories = find_max_calories_elf(elves)
print("elf carrying most calories")
print(max_elf)
print(max_elf_calories)

# challenge 2
df_elves = ranked_calories_elf(elves)
print("calories of top 3 elves")
print(sum(df_elves.iloc[0:3, 0]))
