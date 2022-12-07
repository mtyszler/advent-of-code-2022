def make_one_range(input_str: str) -> range:
    """

    Args:
        input_str: X-Y

    Returns:
        range(X, Y+1)

    """
    start, end = input_str.split(sep="-")

    return range(int(start), int(end) + 1)


def make_ranges(input_str: str) -> [range, range]:
    """

    Args:
        input_str: X-Y, Z-W

    Returns:
        range_1 (X, Y+1), range_2(Z-W+1)

    """

    chunk_1, chunk_2 = input_str.split(sep=',')

    return make_one_range(chunk_1), make_one_range(chunk_2)


def is_contained(input_str: str) -> bool:
    """

    Args:
        input_str: X-Y, Z-W

    Returns:
        True if range1 within range2 or vice-versa
    """

    range_1, range_2 = make_ranges(input_str)

    overlap = set(range_1) & set(range_2)
    if overlap == set(range_1) or overlap == set(range_2):
        return True
    else:
        return False


def has_overlap(input_str: str) -> bool:
    """

    Args:
        input_str: X-Y, Z-W

    Returns:
        True if range1 overlaps range2
    """

    range_1, range_2 = make_ranges(input_str)

    overlap = set(range_1) & set(range_2)
    if overlap == set():
        return False
    else:
        return True
