from collections import defaultdict
nb_shoes = int(input())
pairs = dict()
for _ in range(nb_shoes):
    size, side = [x for x in input().split()]
    if not size in pairs:
        pairs[size] = [0, 0]
    pairs[size][side=="L"] += 1
cnt = 0
for i in pairs.keys():
    cnt += min(pairs[i])
print(cnt)
