import numpy as np


def parse_pairs(input_file: str) -> list:
    """

    Args:
        input_file:

    Returns:
       list of pairs list
    """

    with open(input_file, 'r') as f:
        lines = f.readlines()

    signals_pairs = []
    this_pair = []
    for line in lines:
        if line == "\n":
            signals_pairs.append(this_pair.copy())
            this_pair = []
            continue
        else:
            this_pair.append(eval(line.strip()))

    signals_pairs.append(this_pair.copy())

    return signals_pairs


def check_order_pairs(signal_pairs: list) -> list:
    """

    Args:
        signal_pairs:

    Returns:

    """

    checks = []
    for pair in signal_pairs:
        checks.append(_check_pair(pair))

    return checks


def _check_pair(pair: list, highest_level: bool = True):
    """

    Args:
        pair:

    Returns:

    """
    check = 0

    part_1 = pair[0]
    part_2 = pair[1]

    if type(part_1) == int and type(part_2) == int:
        if part_1 < part_2:
            check = 1
        elif part_1 > part_2:
            check = -1
    elif type(part_1) == int and type(part_2) == list:
        check = _check_pair([[part_1], part_2], highest_level=False)
    elif type(part_1) == list and type(part_2) == int:
        check = _check_pair([part_1, [part_2]], highest_level=False)
    elif type(part_1) == list and type(part_2) == list:
        if len(part_1) < len(part_2):
            preference = -1
        elif len(part_1) > len(part_2):
            preference = 1
        else:
            preference = 0

        for left, right in zip(part_1, part_2):
            check = _check_pair([left, right], highest_level=False)
            if check != 0:
                break

        if preference == -1:
            check = 1 if check == 0 else check
        elif preference == 1:
            check = -1 if check == 0 else check

    if highest_level:
        return True if check >= 0 else False
    else:
        return check


def parse_pairs_v2(input_file: str) -> list:
    """

    Args:
        input_file:

    Returns:
       list of pairs list
    """

    with open(input_file, 'r') as f:
        lines = f.readlines()

    packets = []
    for line in lines:
        if line == "\n":
            continue
        else:
            packets.append(eval(line.strip()))

    return packets


def reorder_packets(packets: list) -> list:
    """

    Args:
        packets:

    Returns:

    """
    old_packets = []
    current_packets = packets.copy()

    while old_packets != current_packets:
        old_packets = current_packets.copy()
        for i in range(len(packets) - 1):
            in_right_order = _check_pair([current_packets[i], current_packets[i+1]])
            if not in_right_order:
                p1 = current_packets[i].copy()
                p2 = current_packets[i + 1].copy()
                current_packets[i] = p2.copy()
                current_packets[i + 1] = p1.copy()

    return current_packets
