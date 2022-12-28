from sympy import solve, Symbol


def decode(input_file: str) -> dict:
    """

    Args:
        input_file:

    Returns:
      list
    """

    monkeys = {}
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        monkey, calling = line.strip().split(sep=": ")
        monkeys[monkey] = int(calling) if calling.isnumeric() else calling

    # solve:
    while not isinstance(monkeys['root'], int):
        for monkey in monkeys.keys():
            if isinstance(monkeys[monkey], int):
                continue

            p1, oper, p2 = monkeys[monkey].split(sep=' ')
            if isinstance(monkeys[p1], int) and isinstance(monkeys[p2], int):
                p1_val = str(monkeys[p1])
                p2_val = str(monkeys[p2])
                monkeys[monkey] = int(eval(p1_val + oper + p2_val))

    return monkeys


def decode_v2(input_file: str) -> list:
    """

    Args:
        input_file:

    Returns:
      list
    """

    monkeys = {}
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        monkey, calling = line.strip().split(sep=": ")
        monkeys[monkey] = int(calling) if calling.isnumeric() else calling

    # error 1: fix root:
    p1, oper, p2 = monkeys['root'].split(sep=' ')
    monkeys['root'] = p1 + ' == ' + p2

    # error 2: fix humn:
    monkeys['humn'] = 'x'

    # solve what can be solved:
    is_solving = True
    while is_solving:
        is_solving = False
        for monkey in monkeys.keys():

            if monkey == 'humn':
                continue
            if isinstance(monkeys[monkey], int):
                continue

            p1, oper, p2 = monkeys[monkey].split(sep=' ')
            if isinstance(monkeys[p1], int) and isinstance(monkeys[p2], int):
                p1_val = str(monkeys[p1])
                p2_val = str(monkeys[p2])
                monkeys[monkey] = int(eval(p1_val + oper + p2_val))
                is_solving = True

    # do substitution:
    is_solving = True
    while is_solving:
        before = len(monkeys['root'])

        original = monkeys['root']
        for x in original.split(sep=' '):
            x = x.strip()
            if len(x) == 4:
                original = original.replace(x, "( " + str(monkeys[x]) + " )")

        monkeys['root'] = original

        after = len(monkeys['root'])

        is_solving = before != after

    x = Symbol('x')
    y = solve(original.replace('==', '-'), x)

    monkeys['humn'] = y[0]

    return monkeys
