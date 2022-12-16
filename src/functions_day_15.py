import numpy as np


def parse_beacon_sensor(input_file: str, size: int, offset_x: int, offset_y: int) -> np.ndarray:
    """

    Args:
        input_file:
        size:
        offset_x:
        offset_y:

    Returns:
       beacon_sensor_map
    """

    """
    0: empty
    1: sensor
    2: beacon
    3: can't be beacon
    """

    map_sensors = np.zeros([size, size], dtype='i')

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        sensor, beacon = line.strip().split(sep=": ")

        # sensor:
        sensor_x, sensor_y = sensor.replace('Sensor at ', '').split(sep=', ')
        sensor_x = int(sensor_x.replace('x=', ''))
        sensor_y = int(sensor_y.replace('y=', ''))

        map_sensors[sensor_y + offset_y, sensor_x + offset_x] = 1

        # beacon:
        beacon_x, beacon_y = beacon.replace('closest beacon is at ', '').split(sep=', ')
        beacon_x = int(beacon_x.replace('x=', ''))
        beacon_y = int(beacon_y.replace('y=', ''))

        map_sensors[beacon_y + offset_y, beacon_x + offset_x] = 2

        manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

        # fill in other cells:
        for xx in range(-manhattan_distance, manhattan_distance + 1):
            for yy in range(-manhattan_distance, manhattan_distance + 1):
                if abs(xx) + abs(yy) > manhattan_distance:
                    continue

                if map_sensors[yy + sensor_y + offset_y, xx + sensor_x + offset_x] == 0:
                    map_sensors[yy + sensor_y + offset_y, xx + sensor_x + offset_x] = 3

    return map_sensors


def parse_beacon_sensor_v2(input_file: str):
    """

    Args:
        input_file:


    Returns:
       beacon_sensor_map
    """

    with open(input_file, 'r') as f:
        lines = f.readlines()

    sensors = []
    beacons = []
    for line in lines:
        sensor, beacon = line.strip().split(sep=": ")

        # sensor:
        sensor_x, sensor_y = sensor.replace('Sensor at ', '').split(sep=', ')
        sensor_x = int(sensor_x.replace('x=', ''))
        sensor_y = int(sensor_y.replace('y=', ''))

        sensor_dict = {'location': [sensor_x, sensor_y]}

        # beacon:
        beacon_x, beacon_y = beacon.replace('closest beacon is at ', '').split(sep=', ')
        beacon_x = int(beacon_x.replace('x=', ''))
        beacon_y = int(beacon_y.replace('y=', ''))

        beacons.append([beacon_x, beacon_y])

        # distance
        manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

        sensor_dict['closest beacon'] = [beacon_x, beacon_y]
        sensor_dict['distance_closest'] = manhattan_distance
        sensors.append(sensor_dict)

    return sensors, beacons


def check_empty(sensors: list[dict], beacons: list[list], question_row: int) -> int:
    """

    Args:
        sensors:
        beacons:
        question_row:

    Returns:

    """
    left_most_x = min([x['location'][0] - x['distance_closest'] for x in sensors])
    right_most_x = max([x['location'][0] + x['distance_closest'] for x in sensors])

    count_cannot = 0
    for i in range(left_most_x, right_most_x + 1):
        for sensor in sensors:
            if [i, question_row] in beacons:
                break
            manhattan_distance = abs(i - sensor['location'][0]) + abs(question_row - sensor['location'][1])
            if manhattan_distance <= sensor['distance_closest']:
                count_cannot += 1
                break

    return count_cannot


def find_missing_beacon(sensors: list[dict], beacons: list[list], max_range: int) -> int:
    """

    Args:
        sensors:
        beacons:
        max_range:

    Returns:

    """
    left_most_x = 0
    right_most_x = max_range

    up_most_y = 0
    down_most_y = max_range

    sensors_locations = [sensor['location'] for sensor in sensors]

    found = False
    x = left_most_x - 1
    while x < right_most_x:
        if found:
            break
        x += 1
        y = up_most_y - 1
        while y < down_most_y:
            if found:
                break
            y += 1
            for sensor in sensors:
                found = True
                if [x, y] in beacons:
                    found = False
                    break
                if [x, y] in sensors_locations:
                    found = False
                    break
                manhattan_distance = abs(x - sensor['location'][0]) + abs(y - sensor['location'][1])
                if manhattan_distance <= sensor['distance_closest']:
                    # cannot be
                    found = False

                    # speed update y:
                    yy = sensor['distance_closest'] - abs(x - sensor['location'][0])
                    ny = yy + sensor['location'][1]
                    # print("(x = ",x,") jump y from", y, " to ", ny)
                    y = ny
                    break

            # if looped all sensors and found no inconsistency:
            if found:
                found_coord = [x, y]
                break

    return found_coord[0] * 4000000 + found_coord[1], found_coord
