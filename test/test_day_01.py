from functions_day_01 import *


def test_import():
    elves_example = parse_input('input_files/input_day_01_example.txt')
    assert(elves_example['elf_3']['food'] == {'food_1': '5000', 'food_2': '6000'})
    assert(elves_example['elf_2']['total_calories'] == 4000)


def test_max():
    elves_example = parse_input('input_files/input_day_01_example.txt')
    max_elf, max_elf_calories = find_max_calories_elf(elves_example)

    assert (max_elf == 'elf_4')
    assert (max_elf_calories == 24000)


def test_ranked():
    elves_example = parse_input('input_files/input_day_01_example.txt')
    df_elves = ranked_calories_elf(elves_example)
    print(df_elves)
    assert (df_elves.iloc[1, ].name == 'elf_3')
    assert (df_elves.iloc[1, ].calories == 11000)
