# Nodes
# 1 2 3 4 5
import numpy as np

# Landmarks:
# (0) Harbor School
# (1) Liggett Hall
# (2) Climate Imaginarium
# (3) Colonel's Row
# (4) Castle Williams
# (5) Fort Jay
Dmat = np.array([
    [0, 600, 850, 500, 850, 1250],
    [600, 0, 350, 450, 1150, 950],
    [830, 350, 0, 450, 1150, 650],
    [500, 450, 450, 0, 750, 750],
    [830, 1150, 1150, 750, 0, 1100],
    [1250, 950, 650, 750, 1100, 0],
    ])

paths = []
# Every path starts at (0) and ends at (5)
# We will then as a group walk from (5) back to (0)

# All paths will then go through either two or three other landmarks
path = "0"
for i in range(1, 5):
    path += str(i)
    for j in range(1, 5):
        if i != j:
            path += str(j)
            for k in range(1, 5):
                if k != i:
                    if k != j:
                        path += str(k) + "5"
                        paths.append(path)
                        path = path[:-2]
                    else:
                        path += "5"
                        paths.append(path)
                        path = path[:-1]
            path = path[:-1]
    path = path[:-1]

# All paths will then go through either one or two other landmarks
# path = "0"
# for i in range(1, 5):
#     path += str(i)
#     for j in range(1, 5):
#         if i != j:
#             path += str(j) + "5"
#             paths.append(path)
#             path = path[:-2]
#         else:
#             path += "5"
#             paths.append(path)
#             path = path[:-1]
#     path = path[:-1]

# See what combination of four paths cover all distances
pairs = []
for i in range(0, 6):
    for j in range(i+1, 6):
        pairs.append(str(i) + str(j))

# We can take these distances when walking back from (5) to (0)
# pairs.remove("35")
# pairs.remove("03")

# Get all combinations for four groups
n_groups = 4
from itertools import combinations
combos = combinations(paths, n_groups)

# Valid combinations have all distances
valid_combos = []
for combo in combos:
    s_combo = ""
    for path in combo:
        s_combo += path
    flag = True
    for pair in pairs:
        if pair not in s_combo and pair[::-1] not in s_combo:
            flag = False
            break
    if flag:
        valid_combos.append(combo)

# Rank the paths by smallest maximum distance requirement
all_dists = []
max_dists = []
for combo in valid_combos:
    dists = []
    for i in range(n_groups):
        dist = 0
        for j in range(len(combo[i])-1):
            dist += Dmat[int(combo[i][j])][int(combo[i][j+1])]
        dists.append(dist)
    max_dists.append(max(dists))
    all_dists.append(tuple(dists))


# Do the sorting
zipped = list(zip(max_dists, valid_combos))
zipped.sort()
_, valid_combos = zip(*zipped)
zipped = list(zip(max_dists, all_dists))
zipped.sort()
max_dists, all_dists = zip(*zipped)
for i, combo in enumerate(valid_combos):
    print(combo, f"Max: {max(all_dists[i])}, All: {tuple(map(int, all_dists[i]))}")
