import numpy as np

def parse24(filename):
    with open(filename) as f:
        data = [l.strip() for l in f.readlines()]
        blizzards = []
        grid = np.zeros((len(data),len(data[0])),dtype=int)
        for r in range(len(data)):
            for c in range(len(data[0])):
                if data[r][c]=="#":
                    grid[r][c]=1
                if data[r][c]!="#" and data[r][c]!=".":
                    blizzards.append((c,r,data[r][c]))
        return grid,blizzards

moves = {">": (+1,0),
         "<": (-1,0),
         "^": (0,-1),
         "v": (0,+1)}

def moveBlizzards(blizzards,xmax,ymax):
    blizzards_new = []
    for x,y,m in blizzards:
        xn,yn = x+moves[m][0],y+moves[m][1]
        if xn==xmax:
            xn=1
        if xn==0:
            xn=xmax-1
        if yn==ymax:
            yn=1
        if yn==0:
            yn=ymax-1
        blizzards_new.append((xn,yn,m))
    return blizzards_new

def paintBlizzards(gridempty,blizzards):
    grid = np.copy(gridempty)
    for x,y,_ in blizzards:
        grid[y][x]+=1
    return grid

def makeGrids(gridempty,blizzards0,verbose=True):
    xmax = gridempty.shape[1]-1
    ymax = gridempty.shape[0]-1
    grid0 = paintBlizzards(gridempty,blizzards0)
    grids = [ grid0 ]
    blizzards = list(blizzards0)
    i = 0
    while True:
        i += 1
        blizzards_new=moveBlizzards(blizzards,xmax,ymax)
        if blizzards_new==blizzards0:
            if verbose:
                print("Found repeating configuration after {} minutes.".format(i))
            return grids
        grid_new = paintBlizzards(gridempty,blizzards_new)
        grids.append(grid_new)
        blizzards = blizzards_new

gridempty,blizzards0 = parse24('../input_files/input_day_24.txt')
grids = makeGrids(gridempty,blizzards0)

from queue import Queue


def adjacents(P, grid):
    '''valid adjacent positions, including current one (i.e. not moving) if possible'''
    xp, yp = P
    adjs = []
    if grid[yp][xp] == 0:
        adjs.append((xp, yp))
    for k, (dx, dy) in moves.items():
        xn = xp + dx
        yn = yp + dy
        if 0 <= xn < len(grid[0]) and 0 <= yn < len(grid) and grid[yn][xn] == 0:
            adjs.append((xn, yn))
    return adjs


def findPath(grids, direction=1, Tstart=0):
    S = (1, 0)
    E = (len(grids[0][0]) - 2, len(grids[0]) - 1)
    if direction == 2:
        S, E = E, S

    q = Queue()
    q.put((Tstart, S))
    explored = set()
    explored.add((Tstart % len(grids), S))

    while not q.empty():
        # get previous position
        T, P = q.get()
        # get blizzard configuration at time T+1
        grid = grids[(T + 1) % len(grids)]
        # enqueue new possible positions
        for A in adjacents(P, grid):
            if A == E:  # reached exit, return elapsed time
                return T + 1
            # re-enque and save already-explored configuration
            if ((T + 1) % len(grids), A) not in explored:
                q.put((T + 1, A))
                explored.add(((T + 1) % len(grids), A))
    return -1


def part1(filename):
    gridempty, blizzards0 = parse24(filename)
    grids = makeGrids(gridempty, blizzards0, verbose=False)
    return findPath(grids, direction=1, Tstart=0)

print(part1('../input_files/input_day_24.txt'))

def part2(filename):
    gridempty,blizzards0 = parse24(filename)
    grids = makeGrids(gridempty,blizzards0,verbose=False)
    T1 = findPath(grids,direction=1,Tstart=0)
    print("Trip 1:",T1)
    T2 = findPath(grids,direction=2,Tstart=T1)
    print("Trip 2:",T2-T1)
    T3 = findPath(grids,direction=1,Tstart=T2)
    print("Trip 3:",T3-T2)
    print("Trip T:",T3)
    return T3

part2("../input_files/input_day_24.txt")