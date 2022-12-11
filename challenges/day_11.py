from functions_day_11 import *

# challenge 1:
monkeys = parse_starting_positions('../input_files/input_day_11.txt')
monkeys = run_monkeys(monkeys, n_rounds=20)

value_monkey_business = monkey_business(monkeys)
print("monkey business")
print(value_monkey_business)

# challenge 2:
monkeys = parse_starting_positions('../input_files/input_day_11.txt')
monkeys = run_monkeys(monkeys, n_rounds=10000, relief=1)

value_monkey_business = monkey_business(monkeys)
print("monkey business")
print(value_monkey_business)