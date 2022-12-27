import re
import time
from copy import deepcopy
import numpy as np


def parse_blueprints(input_file: str) -> list:
    """

    Args:
        input_file:

    Returns:
      list of dictionaries
    """

    archetype = {"id": np.nan,
                 "ore": {"ore": np.nan, "clay": 0, "obsidian": 0},
                 "clay": {"ore": np.nan, "clay": 0, "obsidian": 0},
                 "obsidian": {"ore": np.nan, "clay": np.nan, "obsidian": 0},
                 "geode": {"ore": np.nan, "clay": 0, "obsidian": np.nan}
                 }

    blueprints = []
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        new_bp = deepcopy(archetype)
        bid, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = re.findall(
            r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.',
            line.strip())[0]

        new_bp['id'] = int(bid)
        new_bp['ore']['ore'] = int(ore_ore)
        new_bp['clay']['ore'] = int(clay_ore)
        new_bp['obsidian']['ore'] = int(obsidian_ore)
        new_bp['obsidian']['clay'] = int(obsidian_clay)
        new_bp['geode']['ore'] = int(geode_ore)
        new_bp['geode']['obsidian'] = int(geode_obsidian)

        blueprints.append(new_bp)

    return blueprints


def optimize_blueprint(blueprint: dict, minutes: int, robots: dict = None, stones: dict = None,
                       this_level: int = 0, dropped: list = []) -> int:
    """

    Args:
        blueprint:
        minutes:
        robots
        stones
        this_level
        dropped

    Returns:
        number of geodes collected
    """

    if robots is None:
        robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
    if stones is None:
        stones = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}

    beste_geode = -1
    for t in range(minutes):
        # if this_level == 0:
        #     print("t is ", t, "this level", this_level, "minutes", minutes, "beste_geode",
        #           max(stones['geode'], beste_geode))

        if beste_geode > -1:
            break

        add_robots = []
        if t < minutes - 1 and _can_create(blueprint, stones, 'geode'):
            # best you can do:
            stones = _build_robot(blueprint, stones, 'geode')
            add_robots.append('geode')

        elif t < minutes - 2 and 'obsidian' not in dropped and _can_create(blueprint, stones, 'obsidian'):
            # choose between
            # a. keep collecting
            # b. create a new obsidian

            # don't build:
            robots_dont = deepcopy(robots)
            stones_dont = deepcopy(stones)
            stones_dont = _collect_stones(robots_dont, stones_dont)
            dropped_dont = deepcopy(dropped)
            dropped_dont.append('obsidian')
            geodes_dont_build = optimize_blueprint(blueprint, minutes=minutes - t - 1,
                                                   robots=robots_dont, stones=stones_dont,
                                                   this_level=this_level + 1,
                                                   dropped=dropped_dont)

            # build:
            robots_build = deepcopy(robots)
            stones_build = deepcopy(stones)
            stones_build = _build_robot(blueprint, stones_build, 'obsidian')
            stones_build = _collect_stones(robots_build, stones_build)
            robots_build['obsidian'] += 1
            geodes_build = optimize_blueprint(blueprint, minutes=minutes - t - 1,
                                              robots=robots_build, stones=stones_build,
                                              this_level=this_level + 1)
            beste_geode = max(geodes_build, geodes_dont_build, beste_geode)
            if geodes_build > geodes_dont_build:
                # build
                stones = _build_robot(blueprint, stones, 'obsidian')
                add_robots.append('obsidian')

            else:
                # don't build
                pass

        elif t < minutes - 3 and 'clay' not in dropped and _can_create(blueprint, stones, 'clay'):
            # choose between
            # a. keep collecting
            # b. create a new clay

            # don't build:
            robots_dont = deepcopy(robots)
            stones_dont = deepcopy(stones)
            stones_dont = _collect_stones(robots_dont, stones_dont)
            dropped_dont = deepcopy(dropped)
            dropped_dont.append('clay')
            geodes_dont_build = optimize_blueprint(blueprint, minutes=minutes - t - 1,
                                                   robots=robots_dont, stones=stones_dont,
                                                   this_level=this_level + 1,
                                                   dropped=dropped_dont)

            # build:
            robots_build = deepcopy(robots)
            stones_build = deepcopy(stones)
            stones_build = _build_robot(blueprint, stones_build, 'clay')
            stones_build = _collect_stones(robots_build, stones_build)
            robots_build['clay'] += 1
            geodes_build = optimize_blueprint(blueprint, minutes=minutes - t - 1,
                                              robots=robots_build, stones=stones_build,
                                              this_level=this_level + 1)
            beste_geode = max(geodes_build, geodes_dont_build, beste_geode)
            if geodes_build > geodes_dont_build:
                # build:
                stones = _build_robot(blueprint, stones, 'clay')
                add_robots.append('clay')

            else:
                # don't build
                pass

        elif t < minutes - 2 and 'ore' not in dropped and _can_create(blueprint, stones, 'ore'):
            # choose between
            # a. keep collecting
            # b. create a new ore

            # don't build:
            robots_dont = deepcopy(robots)
            stones_dont = deepcopy(stones)
            stones_dont = _collect_stones(robots_dont, stones_dont)
            dropped_dont = deepcopy(dropped)
            dropped_dont.append('ore')
            geodes_dont_build = optimize_blueprint(blueprint, minutes=minutes - t - 1,
                                                   robots=robots_dont, stones=stones_dont,
                                                   this_level=this_level + 1,
                                                   dropped=dropped_dont)

            # build:
            robots_build = deepcopy(robots)
            stones_build = deepcopy(stones)
            stones_build = _build_robot(blueprint, stones_build, 'ore')
            stones_build = _collect_stones(robots_build, stones_build)
            robots_build['ore'] += 1
            geodes_build = optimize_blueprint(blueprint, minutes=minutes - t - 1,
                                              robots=robots_build, stones=stones_build,
                                              this_level=this_level + 1)
            beste_geode = max(geodes_build, geodes_dont_build, beste_geode)
            if geodes_build > geodes_dont_build:
                # build:
                stones = _build_robot(blueprint, stones, 'ore')
                add_robots.append('ore')
            else:
                # don't build
                pass

        else:
            # nothing to do:
            pass

        stones = _collect_stones(robots, stones)
        for robot in add_robots:
            robots[robot] += 1

    return max(stones['geode'], beste_geode)


def _collect_stones(robots: dict, stones: dict) -> dict:
    """

    Args:
        robots:
        stones:

    Returns:

    """

    for t in ['ore', 'clay', 'obsidian', 'geode']:
        stones[t] += robots[t]

    return stones


def _build_robot(blueprint: dict, stones: dict, robot: str) -> dict:
    """

    Args:
        blueprint:
        stones:
        robot:

    Returns:

    """
    for t in ['ore', 'clay', 'obsidian']:
        stones[t] -= blueprint[robot][t]

    return stones


def _can_create(blueprint: dict, stones: dict, robot: str) -> bool:
    """

    Args:
        blueprint:
        stones:
        robot:

    Returns:

    """

    if blueprint[robot]['ore'] <= stones['ore'] and \
            blueprint[robot]['clay'] <= stones['clay'] and \
            blueprint[robot]['obsidian'] <= stones['obsidian']:
        return True
    else:
        return False


def back_up_optimize_blueprint(blueprint: dict, minutes: int) -> int:
    """

    Args:
        blueprint:
        minutes:

    Returns:
        number of geodes collected
    """

    robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
    stones = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}

    for t in range(minutes):

        add_robots = []
        if _can_create(blueprint, stones, 'geode'):
            # best you can do:
            stones = _build_robot(blueprint, stones, 'geode')
            add_robots.append('geode')

        elif _can_create(blueprint, stones, 'obsidian'):
            # choose between
            # a. keep collecting to build geode
            # b. create a new obsidian

            if robots['obsidian'] > 0:
                # time needed to create a geode if keep collecting:
                t_keep_collecting_for_geode = max(
                    np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                             robots['obsidian']) / robots['obsidian']),
                    np.ceil((blueprint['geode']['ore'] - stones['ore'] -
                             robots['ore']) / robots['ore']))

            else:
                t_keep_collecting_for_geode = np.inf

            # time needed to create a geode if build a new obsidian:
            t_build_obsidian_for_geode = max(
                np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                         robots['obsidian']) / (robots['obsidian'] + 1)),
                np.ceil((blueprint['geode']['ore'] - stones['ore'] + blueprint['obsidian']['ore'] -
                         robots['ore']) / robots['ore']))

            if t_build_obsidian_for_geode <= t_keep_collecting_for_geode:
                # build:
                stones = _build_robot(blueprint, stones, 'obsidian')
                add_robots.append('obsidian')

            else:
                # don't build
                pass

        elif _can_create(blueprint, stones, 'clay'):
            # choose between
            # a. keep collecting to build geode
            # b. keep collecting to build obsidian
            # b. create a new clay

            if robots['clay'] > 0:
                # geode:
                # time needed to create a geode if keep collecting:
                if robots['obsidian'] > 0:
                    t_keep_collecting_for_geode = max(
                        np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                                 robots['obsidian']) / robots['obsidian']),
                        np.ceil((blueprint['geode']['ore'] - stones['ore'] -
                                 robots['ore']) / robots['ore']))

                    # time needed to create a geode if build a new clay:
                    t_build_clay_for_geode = max(
                        np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                                 robots['obsidian']) / robots['obsidian']),
                        np.ceil((blueprint['geode']['ore'] - stones['ore'] + blueprint['clay']['ore'] -
                                 robots['ore']) / robots['ore']))
                else:
                    t_keep_collecting_for_geode = np.inf
                    t_build_clay_for_geode = np.inf

                # obsidian:
                # time needed to create an obsidian if keep collecting:
                t_keep_collecting_obsidian = max(
                    np.ceil((blueprint['obsidian']['clay'] - stones['clay'] - robots['clay']) / robots['clay']),
                    np.ceil((blueprint['obsidian']['ore'] - stones['ore'] - robots['ore']) / robots['ore']))

                # time needed to create an obsidian if build a new clay:
                t_build_clay_for_obsidian = max(
                    np.ceil((blueprint['obsidian']['clay'] - stones['clay'] -
                             robots['clay']) / (robots['clay'] + 1)),
                    np.ceil((blueprint['obsidian']['ore'] - stones['ore'] + blueprint['clay']['ore'] -
                             robots['ore']) / robots['ore']))

            else:
                t_build_clay_for_obsidian = 0
                t_build_clay_for_geode = 0
                t_keep_collecting_obsidian = np.inf
                t_keep_collecting_for_geode = np.inf

            if t_build_clay_for_obsidian <= t_keep_collecting_obsidian and \
                    t_build_clay_for_geode <= t_keep_collecting_for_geode:
                # build:
                stones = _build_robot(blueprint, stones, 'clay')
                add_robots.append('clay')

            else:
                # don't build
                pass

        elif _can_create(blueprint, stones, 'ore'):
            # choose between
            # a. keep collecting to build clay
            # b. keep collecting to build obsidian
            # c. keep collecting to build geode
            # d. create a new ore

            # geode:
            # time needed to create a geode if keep collecting:
            if robots['obsidian'] > 0:
                t_keep_collecting_for_geode = max(
                    np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                             robots['obsidian']) / robots['obsidian']),
                    np.ceil((blueprint['geode']['ore'] - stones['ore'] -
                             robots['ore']) / robots['ore']))

                # time needed to create a geode if build a new ore:
                t_build_ore_for_geode = max(
                    np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                             robots['obsidian']) / robots['obsidian']),
                    np.ceil((blueprint['geode']['ore'] - stones['ore'] + blueprint['ore']['ore'] -
                             robots['ore']) / (robots['ore'] + 1)))
            else:
                t_keep_collecting_for_geode = np.inf
                t_build_ore_for_geode = np.inf

            # obsidian:
            # time needed to create an obsidian if keep collecting:
            if robots['clay'] > 0:
                t_keep_collecting_obsidian = max(
                    np.ceil((blueprint['obsidian']['clay'] - stones['clay'] - robots['clay']) / robots['clay']),
                    np.ceil((blueprint['obsidian']['ore'] - stones['ore'] - robots['ore']) / robots['ore']))

                # time needed to create an obsidian if build a new ore:
                t_build_ore_for_obsidian = max(
                    np.ceil((blueprint['obsidian']['clay'] - stones['clay'] - robots['clay']) / robots['clay']),
                    np.ceil((blueprint['obsidian']['ore'] - stones['ore'] + blueprint['ore']['ore'] -
                             robots['ore']) / (robots['ore'] + 1)))
            else:
                t_keep_collecting_obsidian = np.inf
                t_build_ore_for_obsidian = np.inf

            # clay:
            # time needed to create a clay if keep collecting:
            t_keep_collecting_for_clay = np.ceil((blueprint['clay']['ore'] - stones['ore'] -
                                                  robots['ore']) / robots['ore'])

            t_build_ore_for_clay = np.ceil((blueprint['clay']['ore'] - stones['ore'] + blueprint['ore']['ore'] -
                                            robots['ore']) / (robots['ore'] + 1))

            if t_build_ore_for_obsidian <= t_keep_collecting_obsidian and \
                    t_build_ore_for_geode <= t_keep_collecting_for_geode and \
                    t_build_ore_for_clay <= t_keep_collecting_for_clay:

                # build:
                stones = _build_robot(blueprint, stones, 'ore')
                add_robots.append('ore')

            else:
                # don't build
                pass

        else:
            # nothing to do:
            pass

        stones = _collect_stones(robots, stones)
        for robot in add_robots:
            robots[robot] += 1

    return stones['geode']


def bk2_optimize_blueprint(blueprint: dict, minutes: int) -> int:
    """

    Args:
        blueprint:
        minutes:

    Returns:
        number of geodes collected
    """

    robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
    stones = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}

    for t in range(minutes):

        add_robots = []
        if _can_create(blueprint, stones, 'geode'):
            # best you can do:
            stones = _build_robot(blueprint, stones, 'geode')
            add_robots.append('geode')

        elif _can_create(blueprint, stones, 'obsidian'):
            # choose between
            # a. keep collecting to build geode
            # b. create a new obsidian

            if robots['obsidian'] > 0:
                # time needed to create a geode if keep collecting:
                t_keep_collecting_for_geode = max(
                    np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                             robots['obsidian']) / robots['obsidian']),
                    np.ceil((blueprint['geode']['ore'] - stones['ore'] -
                             robots['ore']) / robots['ore']))

            else:
                t_keep_collecting_for_geode = np.inf

            # time needed to create a geode if build a new obsidian:
            t_build_obsidian_for_geode = max(
                np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                         robots['obsidian']) / (robots['obsidian'] + 1)),
                np.ceil((blueprint['geode']['ore'] - stones['ore'] + blueprint['obsidian']['ore'] -
                         robots['ore']) / robots['ore']))

            if t_build_obsidian_for_geode <= t_keep_collecting_for_geode:
                # build:
                stones = _build_robot(blueprint, stones, 'obsidian')
                add_robots.append('obsidian')

            else:
                # don't build
                pass

        elif _can_create(blueprint, stones, 'clay'):
            # choose between
            # a. keep collecting to build geode
            # b. keep collecting to build obsidian
            # b. create a new clay

            if robots['clay'] > 0:
                # geode:
                # time needed to create a geode if keep collecting:
                if robots['obsidian'] > 0:
                    t_keep_collecting_for_geode = max(
                        np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                                 robots['obsidian']) / robots['obsidian']),
                        np.ceil((blueprint['geode']['ore'] - stones['ore'] -
                                 robots['ore']) / robots['ore']))

                    # time needed to create a geode if build a new clay:
                    t_build_clay_for_geode = max(
                        np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                                 robots['obsidian']) / robots['obsidian']),
                        np.ceil((blueprint['geode']['ore'] - stones['ore'] + blueprint['clay']['ore'] -
                                 robots['ore']) / robots['ore']))
                else:
                    t_keep_collecting_for_geode = np.inf
                    t_build_clay_for_geode = np.inf

                # obsidian:
                # time needed to create an obsidian if keep collecting:
                t_keep_collecting_obsidian = max(
                    np.ceil((blueprint['obsidian']['clay'] - stones['clay'] - robots['clay']) / robots['clay']),
                    np.ceil((blueprint['obsidian']['ore'] - stones['ore'] - robots['ore']) / robots['ore']))

                # time needed to create an obsidian if build a new clay:
                t_build_clay_for_obsidian = max(
                    np.ceil((blueprint['obsidian']['clay'] - stones['clay'] -
                             robots['clay']) / (robots['clay'] + 1)),
                    np.ceil((blueprint['obsidian']['ore'] - stones['ore'] + blueprint['clay']['ore'] -
                             robots['ore']) / robots['ore']))

            else:
                t_build_clay_for_obsidian = 0
                t_build_clay_for_geode = 0
                t_keep_collecting_obsidian = np.inf
                t_keep_collecting_for_geode = np.inf

            if t_build_clay_for_obsidian <= t_keep_collecting_obsidian:
                # build:
                stones = _build_robot(blueprint, stones, 'clay')
                add_robots.append('clay')

            else:
                # don't build
                pass

        elif _can_create(blueprint, stones, 'ore'):
            # choose between
            # a. keep collecting to build clay
            # b. keep collecting to build obsidian
            # c. keep collecting to build geode
            # d. create a new ore

            # geode:
            # time needed to create a geode if keep collecting:
            if robots['obsidian'] > 0:
                t_keep_collecting_for_geode = max(
                    np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                             robots['obsidian']) / robots['obsidian']),
                    np.ceil((blueprint['geode']['ore'] - stones['ore'] -
                             robots['ore']) / robots['ore']))

                # time needed to create a geode if build a new ore:
                t_build_ore_for_geode = max(
                    np.ceil((blueprint['geode']['obsidian'] - stones['obsidian'] -
                             robots['obsidian']) / robots['obsidian']),
                    np.ceil((blueprint['geode']['ore'] - stones['ore'] + blueprint['ore']['ore'] -
                             robots['ore']) / (robots['ore'] + 1)))
            else:
                t_keep_collecting_for_geode = np.inf
                t_build_ore_for_geode = np.inf

            # obsidian:
            # time needed to create an obsidian if keep collecting:
            if robots['clay'] > 0:
                t_keep_collecting_obsidian = max(
                    np.ceil((blueprint['obsidian']['clay'] - stones['clay'] - robots['clay']) / robots['clay']),
                    np.ceil((blueprint['obsidian']['ore'] - stones['ore'] - robots['ore']) / robots['ore']))

                # time needed to create an obsidian if build a new ore:
                t_build_ore_for_obsidian = max(
                    np.ceil((blueprint['obsidian']['clay'] - stones['clay'] - robots['clay']) / robots['clay']),
                    np.ceil((blueprint['obsidian']['ore'] - stones['ore'] + blueprint['ore']['ore'] -
                             robots['ore']) / (robots['ore'] + 1)))
            else:
                t_keep_collecting_obsidian = np.inf
                t_build_ore_for_obsidian = np.inf

            # clay:
            # time needed to create a clay if keep collecting:
            t_keep_collecting_for_clay = np.ceil((blueprint['clay']['ore'] - stones['ore'] -
                                                  robots['ore']) / robots['ore'])

            t_build_ore_for_clay = np.ceil((blueprint['clay']['ore'] - stones['ore'] + blueprint['ore']['ore'] -
                                            robots['ore']) / (robots['ore'] + 1))

            if t_build_ore_for_clay <= t_keep_collecting_for_clay:

                # build:
                stones = _build_robot(blueprint, stones, 'ore')
                add_robots.append('ore')

            else:
                # don't build
                pass

        else:
            # nothing to do:
            pass

        stones = _collect_stones(robots, stones)
        for robot in add_robots:
            robots[robot] += 1

    return stones['geode']


def all_bp(blueprints: list, minutes: int) -> dict:
    """

    Args:
        blueprints:
        minutes:

    Returns:

    """
    results = {}
    for bp in blueprints:
        st = time.time()
        geode = optimize_blueprint(bp, minutes=minutes)
        results[bp['id']] = geode
        elapsed_time = time.time() - st
        print(bp['id'], 'Execution time:', elapsed_time, 'seconds (', geode, ')')

    return results
