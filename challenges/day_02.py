from functions_day_02 import *

strategy_guide = read_in_rps_strategy_guide('../input_files/input_day_02.txt')
score = compute_score_rsp_strategy(strategy_guide)

print("Strategy guide score")
print(score)

score_v2 = compute_score_rsp_strategy_v2(strategy_guide)

print("Strategy guide score v2")
print(score_v2)
