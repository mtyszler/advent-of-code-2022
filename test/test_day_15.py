import pytest

from functions_day_15 import *


def test_parse_beacon_sensor():
    map_sensors = parse_beacon_sensor('input_files/input_day_15_example.txt', size=50, offset_x=2, offset_y=0)


def test_parse_beacon_sensor_cannot():
    offset_x = 2
    offset_y = 0
    map_sensors = parse_beacon_sensor('input_files/input_day_15_example.txt', size=50,
                                      offset_x=offset_x, offset_y=offset_y)

    assert (sum(map_sensors[10 + offset_y, :] == 3) == 26)


def test_parse_beacon_sensor_v2():
    sensors, beacons = parse_beacon_sensor_v2('input_files/input_day_15_example.txt')

    print(sensors)


def test_parse_beacon_sensor_cannot_v2():
    sensors, beacons = parse_beacon_sensor_v2('input_files/input_day_15_example.txt')

    count_cannot = check_empty(sensors, beacons, question_row=10)

    assert (count_cannot == 26)


def test_find_beacon():
    sensors, beacons = parse_beacon_sensor_v2('input_files/input_day_15_example.txt')

    tuning_freq, beacon_coord = find_missing_beacon(sensors, beacons, max_range=20)

    assert (tuning_freq == 56000011)
    assert (beacon_coord[0] == 14)
    assert (beacon_coord[1] == 11)
