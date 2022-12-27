import numpy as np

from functions_day_20 import *

decoded = decode('../input_files/input_day_20.txt', decription_key=1, n_mix=1)

after = [x['value'] for x in decoded]

zero_index = np.argwhere(np.array(after) == 0)[0][0]
pos = 1000 + zero_index
index = ((pos + 1) % len(decoded)) - 1
p1 = after[index]
pos = 2000 + zero_index
index = ((pos + 1) % len(decoded)) - 1
p2 = after[index]
pos = 3000 + zero_index
index = ((pos + 1) % len(decoded)) - 1
p3 = after[index]

print(p1, p2, p3)
s = p1 + p2 + p3
print(s)

# part 2:
decoded = decode('../input_files/input_day_20.txt', decription_key=811589153, n_mix=10)

after = [x['value'] for x in decoded]

zero_index = np.argwhere(np.array(after) == 0)[0][0]
pos = 1000 + zero_index
index = ((pos + 1) % len(decoded)) - 1
p1 = after[index]
pos = 2000 + zero_index
index = ((pos + 1) % len(decoded)) - 1
p2 = after[index]
pos = 3000 + zero_index
index = ((pos + 1) % len(decoded)) - 1
p3 = after[index]

print(p1, p2, p3)
s = p1 + p2 + p3
print(s)