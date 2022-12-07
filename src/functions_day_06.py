def find_starter_of_marker(input_str: str, signal_length: int, occurrence: int) -> [int, str]:
    """

    Args:
        input_str:
        signal_length:
        occurrence:

    Returns:

    """

    this_occurrence = 0
    start = 0
    while this_occurrence < occurrence:
        for i in range(len(input_str)):
            if start + signal_length > len(input_str):
                raise ValueError('No signal found')

            candidate = input_str[start:start + signal_length]
            if len(set(candidate)) == signal_length:
                signal_pos = start + signal_length
                signal_str = candidate
                this_occurrence += 1
                break
            else:
                start += 1

    return signal_pos, signal_str
