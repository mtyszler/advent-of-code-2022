import copy
import time

from functions_day_19 import *

blueprints = parse_blueprints('../input_files/input_day_19.txt')
# blueprints = parse_blueprints('../input_files/input_day_19_example.txt')
st = time.time()
stones_1 = optimize_blueprint(blueprints[3], minutes=24)
print(stones_1)
elapsed_time = time.time() - st
print('Execution time:', elapsed_time, 'seconds')

all_results = all_bp(blueprints, minutes=24)
indicator = sum([int(k)*v for k, v in all_results.items()])
print('Part 1')
print(indicator) # 1641, something wrong with bp id 4 15 and 18

stones_21 = optimize_blueprint(blueprints[0], minutes=32)
stones_22 = optimize_blueprint(blueprints[1], minutes=32)
stones_23 = optimize_blueprint(blueprints[2], minutes=32)
print('Part 2')
print(stones_21, stones_22, stones_23)
print(stones_21 * stones_22 * stones_23) # 41, 11, 28 = 12626
