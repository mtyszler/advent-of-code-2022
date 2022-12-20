from copy import deepcopy
import re
import numpy as np


def parse_pipes(input_file: str) -> dict:
    """

    Args:
        input_file:

    Returns:
       dict with pipes
    """

    pipes = {}

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        valve, flow_rate, leads = re.findall(r'Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.*)',
                                             line.strip())[0]
        print(valve)
        pipes[valve] = {}
        pipes[valve]['flow_rate'] = int(flow_rate)
        pipes[valve]['leads_to'] = [x.strip() for x in leads.split(sep=",")]

    return pipes


def best_route(pipes: dict, minutes: int):
    """

    Args:
        pipes:
        minutes:

    Returns:

    """
    valves_can_be_open = [valve for valve in pipes.keys() if pipes[valve]['flow_rate'] > 0]
    n_valves_can_be_open = len(valves_can_be_open)

    working_paths = [{'route': ['AA'], 'clock': 0, 'pressure': 0, 'opened_valves': []}]
    in_expansion = True

    count_rounds = 0
    while in_expansion and count_rounds < minutes:
        current_max = max([path['pressure'] for path in working_paths])
        count_rounds += 1
        print("round", count_rounds)
        in_expansion = False
        new_working_paths = []

        for path in working_paths:

            # if time is up:
            if path['clock'] >= minutes:
                new_path = deepcopy(path)
                new_working_paths.append(new_path)
                continue

            # check potential pressure:
            unopened_pressures = sorted([pipes[valve]['flow_rate'] for valve in pipes.keys() if
                                         valve not in path['opened_valves'] and pipes[valve]['flow_rate'] > 0],
                                        reverse=True)
            potential_pressure = path['pressure']
            tick_count = 1
            for fr in unopened_pressures:
                potential_pressure += fr * (minutes - path['clock'] - tick_count)
                tick_count += 2
                if minutes - path['clock'] - tick_count < 0:
                    break

            if potential_pressure < current_max:
                # drop path
                continue

            # if all valves have been opened:
            if len(path['opened_valves']) == n_valves_can_be_open:
                new_path = deepcopy(path)
                new_working_paths.append(new_path)
                continue

            valve = path['route'][-1]

            if len(path['route']) >= 2 and path['route'][-1] not in path['opened_valves']:
                if pipes[valve]['flow_rate'] > 0:
                    # open valve:
                    in_expansion = True
                    new_path = deepcopy(path)
                    new_path['route'].append(valve)
                    new_path['opened_valves'].append(valve)
                    new_path['clock'] += 1
                    new_path['pressure'] += pipes[valve]['flow_rate'] * (minutes - new_path['clock'])
                    new_working_paths.append(new_path)

            for lead in pipes[valve]['leads_to']:
                if lead in path['route']:
                    # don't make a pointless loop
                    # between last time the lead has been visited and now a valve must have been opened:

                    # find last visit to lead
                    pos = path['route'].index(lead, 0)
                    remaining = path['route'][pos + 1:]
                    while lead in remaining:
                        pos = path['route'].index(lead, pos + 1)
                        remaining = path['route'][pos + 1:]

                    if len(remaining) == len(set(remaining)):
                        # no valve was opened
                        continue

                # move to new position
                in_expansion = True
                new_path = deepcopy(path)
                new_path['route'].append(lead)
                new_path['clock'] += 1
                new_working_paths.append(new_path)

        working_paths = deepcopy(new_working_paths)
        print("current max:", max([path['pressure'] for path in working_paths]))

    # find best:
    best_pressure = 0
    best_path = []

    for path in working_paths:
        if path['pressure'] > best_pressure:
            best_path = path['route'].copy()
            best_pressure = path['pressure']

    return best_pressure, best_path


def best_route_together(pipes: dict, minutes: int):
    """

    Args:
        pipes:
        minutes:

    Returns:

    """
    valves_can_be_open = [valve for valve in pipes.keys() if pipes[valve]['flow_rate'] > 0]
    n_valves_can_be_open = len(valves_can_be_open)

    working_paths = [{'route_1': ['AA'], 'route_2': ['AA'], 'clock': 0, 'pressure': 0, 'opened_valves': []}]
    in_expansion = True

    count_rounds = 0
    while in_expansion and count_rounds < minutes:
        current_max = max([path['pressure'] for path in working_paths])
        count_rounds += 1
        print("round", count_rounds)
        print("starting with", len(working_paths),"paths")
        in_expansion = False
        new_working_paths = []
        new_to_carry_paths = []

        for path in working_paths:

            # if time is up:
            if path['clock'] >= minutes:
                new_path = deepcopy(path)
                new_working_paths.append(new_path)
                continue

            # check potential pressure:
            unopened_pressures = sorted([pipes[valve]['flow_rate'] for valve in pipes.keys() if
                                         valve not in path['opened_valves'] and pipes[valve]['flow_rate'] > 0],
                                        reverse=True)
            unopened_valves = [valve for valve in pipes.keys() if
                               valve not in path['opened_valves'] and pipes[valve]['flow_rate'] > 0]
            potential_pressure = path['pressure']
            if potential_pressure < current_max/2:  # see if cutting low performing paths is helpful
                # drop path
                continue
            tick_count = 1
            if path['route_1'][-1] not in unopened_valves and path['route_2'][-1] not in unopened_valves:
                tick_count += 1
            person_1 = True
            for fr in unopened_pressures:
                potential_pressure += fr * (minutes - path['clock'] - tick_count)
                if person_1:
                    person_1 = False
                else:
                    person_1 = True
                    tick_count += 2
                if minutes - path['clock'] - tick_count < 0:
                    break

            if potential_pressure < current_max:
                # drop path
                continue

            # if all valves have been opened:
            if len(path['opened_valves']) == n_valves_can_be_open:
                new_path = deepcopy(path)
                new_working_paths.append(new_path)
                continue

            # expand on the basis of route_1 and for each route_1, expand route_2
            new_draft_paths = []
            valve_1 = path['route_1'][-1]

            if len(path['route_1']) >= 2 and path['route_1'][-1] not in path['opened_valves']:
                if pipes[valve_1]['flow_rate'] > 0:
                    # open valve:
                    # in_expansion = True
                    new_path = deepcopy(path)
                    new_path['route_1'].append(valve_1)
                    new_path['opened_valves'].append(valve_1)
                    new_path['clock'] += 1
                    new_path['pressure'] += pipes[valve_1]['flow_rate'] * (minutes - new_path['clock'])
                    new_draft_paths.append(new_path)

            for lead in pipes[valve_1]['leads_to']:
                if lead in path['route_1']:
                    # don't make a pointless loop
                    # between last time the lead has been visited and now a valve must have been opened:

                    # find last visit to lead
                    pos = path['route_1'].index(lead, 0)
                    remaining = path['route_1'][pos + 1:]
                    while lead in remaining:
                        pos = path['route_1'].index(lead, pos + 1)
                        remaining = path['route_1'][pos + 1:]

                    if len(remaining) == len(set(remaining)):
                        # no valve was opened
                        continue

                # move to new position
                # in_expansion = True
                new_path = deepcopy(path)
                new_path['route_1'].append(lead)
                new_path['clock'] += 1
                new_draft_paths.append(new_path)

            # expand route_2 based on the new potential route_1, avoiding duplicates
            for potential_path in new_draft_paths:
                valve_2 = potential_path['route_2'][-1]

                if len(potential_path['route_2']) >= 2 and \
                        potential_path['route_2'][-1] not in potential_path['opened_valves']:
                    if pipes[valve_2]['flow_rate'] > 0:
                        # open valve:
                        new_path = deepcopy(potential_path)
                        new_path['route_2'].append(valve_2)
                        new_path['opened_valves'].append(valve_2)
                        # new_path['clock'] += 1
                        new_path['pressure'] += pipes[valve_2]['flow_rate'] * (minutes - new_path['clock'])

                        # avoid duplicates:
                        skip = False
                        if new_path['route_1'] == new_path['route_2']:
                            skip = True

                        for to_compare_path in new_to_carry_paths:
                            if ((new_path['route_1'] == to_compare_path['route_1']) and
                                (new_path['route_2'] == to_compare_path['route_2'])) or \
                                ((new_path['route_2'] == to_compare_path['route_1']) and
                                 (new_path['route_1'] == to_compare_path['route_2'])):
                                skip = True

                        for to_compare_path in new_working_paths:
                            if ((new_path['route_1'] == to_compare_path['route_1']) and
                                (new_path['route_2'] == to_compare_path['route_2'])) or \
                                ((new_path['route_2'] == to_compare_path['route_1']) and
                                 (new_path['route_1'] == to_compare_path['route_2'])):
                                skip = True

                        if not skip:
                            new_to_carry_paths.append(new_path)
                            in_expansion = True

                for lead in pipes[valve_2]['leads_to']:
                    if lead in potential_path['route_2']:
                        # don't make a pointless loop
                        # between last time the lead has been visited and now a valve must have been opened:

                        # find last visit to lead
                        pos = potential_path['route_2'].index(lead, 0)
                        remaining = potential_path['route_2'][pos + 1:]
                        while lead in remaining:
                            pos = potential_path['route_2'].index(lead, pos + 1)
                            remaining = potential_path['route_2'][pos + 1:]

                        if len(remaining) == len(set(remaining)):
                            # no valve was opened
                            continue

                    # move to new position
                    new_path = deepcopy(potential_path)
                    new_path['route_2'].append(lead)
                    # new_path['clock'] += 1

                    # avoid duplicates:
                    skip = False
                    if new_path['route_1'] == new_path['route_2']:
                        skip = True

                    for to_compare_path in new_to_carry_paths:
                        if ((new_path['route_1'] == to_compare_path['route_1']) and
                            (new_path['route_2'] == to_compare_path['route_2'])) or \
                                ((new_path['route_2'] == to_compare_path['route_1']) and
                                 (new_path['route_1'] == to_compare_path['route_2'])):
                            skip = True

                    for to_compare_path in new_working_paths:
                        if ((new_path['route_1'] == to_compare_path['route_1']) and
                            (new_path['route_2'] == to_compare_path['route_2'])) or \
                                ((new_path['route_2'] == to_compare_path['route_1']) and
                                 (new_path['route_1'] == to_compare_path['route_2'])):
                            skip = True

                    if not skip:
                        new_to_carry_paths.append(new_path)
                        in_expansion = True

        for to_carry in new_to_carry_paths:
            new_working_paths.append(deepcopy(to_carry))
        working_paths = deepcopy(new_working_paths)
        print("current max:", max([path['pressure'] for path in working_paths]))

    # find best:
    best_pressure = 0
    best_path = []

    for path in working_paths:
        if path['pressure'] > best_pressure:
            best_path = [path['route_1'].copy(), path['route_2'].copy()]
            best_pressure = path['pressure']

    return best_pressure, best_path


def best_route_with_2(pipes: dict, minutes: int):
    """

    Args:
        pipes:
        minutes:

    Returns:

    """
    valves_can_be_open = [valve for valve in pipes.keys() if pipes[valve]['flow_rate'] > 0]
    n_valves_can_be_open = len(valves_can_be_open)

    working_paths = [{'route': ['AA'], 'clock': 0, 'pressure': 0, 'opened_valves': []}]
    in_expansion = True

    count_rounds = 0
    while in_expansion and count_rounds < minutes:
        current_max = max([path['pressure'] for path in working_paths])
        try:
            current_max_2nd = max([path['pressure'] for path in working_paths if path['pressure'] != current_max])
        except:
            current_max_2nd = current_max
        count_rounds += 1
        print("round", count_rounds)
        in_expansion = False
        new_working_paths = []

        for path in working_paths:

            # if time is up:
            if path['clock'] >= minutes:
                new_path = deepcopy(path)
                new_working_paths.append(new_path)
                continue

            # check potential pressure:
            unopened_pressures = sorted([pipes[valve]['flow_rate'] for valve in pipes.keys() if
                                         valve not in path['opened_valves'] and pipes[valve]['flow_rate'] > 0],
                                        reverse=True)
            potential_pressure = path['pressure']
            tick_count = 1
            for fr in unopened_pressures:
                potential_pressure += fr * (minutes - path['clock'] - tick_count)
                tick_count += 2
                if minutes - path['clock'] - tick_count < 0:
                    break

            if potential_pressure < current_max_2nd:
                # drop path
                continue

            # if all valves have been opened:
            if len(path['opened_valves']) == n_valves_can_be_open:
                new_path = deepcopy(path)
                new_working_paths.append(new_path)
                continue

            valve = path['route'][-1]

            if len(path['route']) >= 2 and path['route'][-1] not in path['opened_valves']:
                if pipes[valve]['flow_rate'] > 0:
                    # open valve:
                    in_expansion = True
                    new_path = deepcopy(path)
                    new_path['route'].append(valve)
                    new_path['opened_valves'].append(valve)
                    new_path['clock'] += 1
                    new_path['pressure'] += pipes[valve]['flow_rate'] * (minutes - new_path['clock'])
                    new_working_paths.append(new_path)

            for lead in pipes[valve]['leads_to']:
                if lead in path['route']:
                    # don't make a pointless loop
                    # between last time the lead has been visited and now a valve must have been opened:

                    # find last visit to lead
                    pos = path['route'].index(lead, 0)
                    remaining = path['route'][pos + 1:]
                    while lead in remaining:
                        pos = path['route'].index(lead, pos + 1)
                        remaining = path['route'][pos + 1:]

                    if len(remaining) == len(set(remaining)):
                        # no valve was opened
                        continue

                # move to new position
                in_expansion = True
                new_path = deepcopy(path)
                new_path['route'].append(lead)
                new_path['clock'] += 1
                new_working_paths.append(new_path)

        working_paths = deepcopy(new_working_paths)
        print("current max:", max([path['pressure'] for path in working_paths]))

    # find best:
    best_pressure = 0
    best_path = []

    second_best_pressure = 0
    second_best_path = []

    for path in working_paths:
        if path['pressure'] > best_pressure:
            best_path = path['route'].copy()
            best_pressure = path['pressure']
        if path['pressure'] > second_best_pressure and path['pressure'] < best_pressure:
            second_best_path = path['route'].copy()
            second_best_pressure = path['pressure']

    return best_pressure, best_path
