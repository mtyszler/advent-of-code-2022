import pandas as pd


# Day 1

def parse_input(filename: str) -> dict:
    """
     convert input file into a dictionary of dictionaries on elves food

    Args:
        filename: txt file if input of elves food
    :return:
        output format:
        elves = {
            food = {
                'food_1': xxx,
                ...


            }
            total_calories: yyy
    """

    input_file = open(filename, 'r')
    lines = input_file.readlines()

    # initialize
    elves = {}
    count_elves = 1
    elves['elf_' + str(count_elves)] = {}
    elves['elf_' + str(count_elves)]['food'] = {}
    count_food = 1
    cum_tot = 0

    for line in lines:

        if line.strip():
            # 'The line is NOT empty
            elves['elf_' + str(count_elves)]['food']['food_' + str(count_food)] = line.strip()
            cum_tot += int(line.strip())
            count_food += 1
        else:
            # The line is empty'
            elves['elf_' + str(count_elves)]['total_calories'] = cum_tot

            # reset
            count_elves += 1
            elves['elf_' + str(count_elves)] = {}
            elves['elf_' + str(count_elves)]['food'] = {}
            count_food = 1
            cum_tot = 0

        if line.strip():
            # The last line is no empty
            elves['elf_' + str(count_elves)]['total_calories'] = cum_tot

    return elves


def find_max_calories_elf(elves: dict) -> [str, int]:
    """
    Find max calories elf

    Args:
         elves: see parse_input
    :return:
        max_calories, max(total_calories.values())
    """
    total_calories = {elf: values['total_calories'] for elf, values in elves.items()}
    max_calories = [key for key, value in total_calories.items() if value == max(total_calories.values())]

    return max_calories[0], max(total_calories.values())


def ranked_calories_elf(elves: dict) -> pd.DataFrame:
    """
    Compute ranked table of elves

    Args:
        elves: see parse_input
    Returns:

        max_calories, max(total_calories.values())
    """

    total_calories = {elf: values['total_calories'] for elf, values in elves.items()}
    df_elves = pd.DataFrame.from_dict(total_calories, orient='index', columns=['calories']).sort_values(by='calories',
                                                                                                        ascending=False)

    return df_elves

