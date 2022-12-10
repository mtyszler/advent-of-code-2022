import numpy as np


def parse_instructions(input_file: str) -> list:
    """

    Args:
        input_file:

    Returns:
        list with values of X in each cycle
    """

    signals = [1]

    with open(input_file, 'r') as f:
        instructions = f.readlines()

    for instruction in instructions:
        if instruction.strip() == 'noop':
            signals.append(signals[-1])

        elif instruction.strip().split()[0] == 'addx':
            signals.append(signals[-1])
            signals.append(signals[-1] + int(instruction.strip().split()[1]))

        else:
            raise ValueError("Unknown instruction")

    return signals


def compute_signal_strength(signals: list, positions: list) -> int:
    """

    Args:
        signals:
        positions:

    Returns:

    """

    scores = [signals[ind - 1] * ind for ind in positions]
    score = sum(scores)

    return score


def make_crt_image(signals: list, sprite_size: int = 3, CRT_length: int = 40) -> np.ndarray:
    """

    Args:
        CRT_length:
        sprite_size:
        signals:

    Returns:

    """

    CRT = np.chararray(len(signals) - 1)
    CRT[:] = '.'

    pixel_pos = 0
    for idx, cycle_value in enumerate(signals[:-1]):
        sprite = np.zeros(CRT_length, dtype='i')
        this_slice = range(max(int(cycle_value - (sprite_size - 1) / 2), 0),
                           min(int(cycle_value + (sprite_size - 1) / 2 + 1), 40))
        sprite[this_slice] = 1
        if sprite[pixel_pos] == 1:
            CRT[idx] = '#'
        pixel_pos += 1
        if pixel_pos == 40:
            pixel_pos = 0

    CRT = np.reshape(CRT, (int(len(CRT)/CRT_length), CRT_length))
    return CRT
