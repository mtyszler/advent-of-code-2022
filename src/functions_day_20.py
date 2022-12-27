def decode(input_file: str, decription_key: int, n_mix: int) -> list:
    """

    Args:
        input_file:
        decription_key

    Returns:
      list
    """

    decoded = []
    with open(input_file, 'r') as f:
        lines = f.readlines()

    i = 0

    for line in lines:
        this_item = {'original_index': i,
                     'value': int(line.strip()) * decription_key}

        decoded.append(this_item)
        i += 1

    for _ in range(n_mix):
        for i in range(len(decoded)):
            if i % 1000 == 0:
                print("scrambling line", i, "of", len(decoded) - 1)
            for current_index, item in enumerate(decoded):
                if item['original_index'] == i:
                    item_of_interest = item
                    break

            amount = item_of_interest['value']
            new_index = (current_index + amount) % (len(decoded) - 1)

            new_item = decoded.pop(current_index)
            decoded.insert(new_index, new_item)

            after = [x['value'] for x in decoded]

    return decoded
