from functions_day_11 import *

# challenge 1:
monkeys, min_common_multiplier = parse_starting_positions('../input_files/input_day_11.txt')
monkeys = run_monkeys(monkeys, n_rounds=20, relief=3, min_common_multiplier=min_common_multiplier)

value_monkey_business = monkey_business(monkeys)
print("monkey business")
print(value_monkey_business)

# challenge 2:
monkeys, min_common_multiplier = parse_starting_positions('../input_files/input_day_11.txt')
monkeys = run_monkeys(monkeys, n_rounds=10000, relief=1, min_common_multiplier=min_common_multiplier, verbose=True)

value_monkey_business = monkey_business(monkeys)
print("monkey business")
print(value_monkey_business)