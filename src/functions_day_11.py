import numpy as np


def parse_starting_positions(input_file: str) -> [list[dict], int]:
    """

    Args:
        input_file:

    Returns:
       list of dict of monkey attributes
    """

    monkeys = []
    first = True
    min_common_multiplier = 1
    with open(input_file, 'r') as f:
        all_monkeys = f.readlines()

    for this_monkey in all_monkeys:
        if this_monkey.strip()[0:6] == "Monkey":
            if first:
                first = False
            else:
                new_monkey['n_inspections'] = 0
                monkeys.append(new_monkey.copy())
            new_monkey = {}

        elif 'Starting items' in this_monkey:
            new_monkey['items'] = [int(item) for item in this_monkey.strip().split(":")[1].split(",")]
        elif 'Operation' in this_monkey:
            new_monkey['operation'] = this_monkey.strip().split(":")[1].split("=")[1].strip()
        elif 'Test' in this_monkey:
            new_monkey['test'] = int(this_monkey.strip().split(":")[1].split("by")[1])
            min_common_multiplier *= int(this_monkey.strip().split(":")[1].split("by")[1])
        elif 'If true' in this_monkey:
            new_monkey['true'] = int(this_monkey.strip().split(":")[1].split("monkey")[1])
        elif 'If false' in this_monkey:
            new_monkey['false'] = int(this_monkey.strip().split(":")[1].split("monkey")[1])
        else:
            pass

    new_monkey['n_inspections'] = 0
    monkeys.append(new_monkey.copy())

    return monkeys, min_common_multiplier


def _monkey_round(monkeys: list[dict], min_common_multiplier: int, relief: int = 3) -> list[dict]:
    """

    Args:
        monkeys:

    Returns:

    """

    for this_monkey in monkeys:

        for this_item in this_monkey['items']:
            this_monkey['n_inspections'] += 1
            worry_level = int(np.floor(eval(this_monkey['operation'], {}, {'old': this_item}) / relief))
            test = np.mod(worry_level, this_monkey['test']) == 0
            if relief == 1:
                to_add_worry_level = int(np.mod(worry_level, min_common_multiplier))
            else:
                to_add_worry_level = worry_level
            if test:
                monkeys[this_monkey['true']]['items'].append(to_add_worry_level)
            else:
                monkeys[this_monkey['false']]['items'].append(to_add_worry_level)
        # clear
        this_monkey['items'] = []

    return monkeys


def run_monkeys(monkeys: list[dict], n_rounds: int, relief: int = 3, min_common_multiplier: int = 1,
                verbose: bool = False) -> list[dict]:
    """

    Args:
        min_common_multiplier:
        verbose:
        relief:
        monkeys:
        n_rounds:

    Returns:

    """

    for i in range(n_rounds):
        if verbose:
            if np.mod(i, 500) == 0:
                print("round ", i)
        monkeys = _monkey_round(monkeys, relief=relief, min_common_multiplier=min_common_multiplier)

    return monkeys


def monkey_business(monkeys: list[dict]) -> int:
    """

    Args:
        monkeys:

    Returns:

    """

    n_inspections = sorted([monkey['n_inspections'] for monkey in monkeys], reverse=True)

    return n_inspections[0] * n_inspections[1]
