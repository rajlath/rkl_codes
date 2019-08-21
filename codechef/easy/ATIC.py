from itertools import groupby
for _ in range(int(input())):
    current = input()
    cg = groupby(current)
    pos = []
    for k, g in cg:
        if k == ".":
            pos.append(len(list(g)))
    maxs = 0
    count= 0
    #print(pos)
    for i in pos:
        if i > maxs:
            count += 1
            maxs = max(maxs, i)
    print(count)
