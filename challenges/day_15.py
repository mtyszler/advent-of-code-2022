from functions_day_15 import *

# # challenge 1:
# sensors, beacons = parse_beacon_sensor_v2('../input_files/input_day_15.txt')
#
# question_row = 2000000
# count_cannot = check_empty(sensors, beacons, question_row=question_row)
#
# print("Cannot have beacons on row", question_row)
# print(count_cannot)

# challenge 2:
sensors, beacons = parse_beacon_sensor_v2('../input_files/input_day_15.txt')

tuning_freq, beacon_coord = find_missing_beacon(sensors, beacons, max_range=4000000)

print("Beacon found at", beacon_coord)
print("Tuning frequency")
print(tuning_freq)

