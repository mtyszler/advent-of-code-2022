import difflib


def find_overlap_rucksack(input_str: str) -> str:
    """
    split string in 2 and find overlap

    Args:
        input_str:

    Returns:
        overlapping str

    """

    N = len(input_str)
    part_1 = input_str[0:int(N / 2)]
    part_2 = input_str[int(N / 2):]

    s = difflib.SequenceMatcher(None, part_1, part_2)
    pos_a, pos_b, size = s.find_longest_match(0, len(part_1), 0, len(part_2))
    return part_1[pos_a:pos_a + size]


def priority_letter(letter: str) -> int:
    """
    a-z: 1 to 26
    A-Z: 27 to 52

    Args:
        letter:

    Returns:
        letter to int
    """

    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26


def find_badges_rucksack(input_str_1: str, input_str_2: str, input_str_3: str) -> str:
    """
   find common letter in 3 strings

    Args:
        input_str_1:
        input_str_2:
        input_str_3:

    Returns:
        overlapping str

    """

    overlap = set(input_str_1) & set(input_str_2) & set(input_str_3)
    # print(overlap)

    return list(overlap)[0]
