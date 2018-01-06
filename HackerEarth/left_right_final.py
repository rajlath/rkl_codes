'''
3 4
1 2 3
0 1 L
1 3 L
2 1 R
1 5 L
city_cnt, query_cnt = [int(x) for x in input().split()]
cities = [int(x) for x in input().split()]
for i in range(query_cnt):
    begins, target, ways = [x for x in input().split()]
    nexts = int(begins)
    target= int(target)
    moves = -1
    found = False
    for i in range(city_cnt):
        #print(cities[nexts], target)
        moves += 1
        if cities[nexts] == target:
            found = True
            break
        else:
            if ways == "R":
                nexts = (nexts + 1)%city_cnt
            else:
                nexts = (nexts - 1 + city_cnt)%city_cnt
    if found:print(moves)
    else:print(-1)
'''
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end




maxn = 2000005
noe, noq = [int(x) for x in input().split()]
noee = noe + 1
type_list = [int(x) for x in input().split()]
type_list = sorted(type_list)
ranks = [0]*maxn
for i in range(maxn):
    ranks[i] = binary_search(type_list, i)




lefts = [[maxn for i in range(noe)] for j in range(noe)]
rights= [[maxn for i in range(noe)] for j in range(noe)]

for i in range(noe):
    pos = i
    steps = 0
    while steps < noe:
        curr =  ranks[type_list[pos]]
        rights[i][curr] = min(rights[i][curr], steps)
        steps += 1
        pos = (pos + 1) % noe

    pos = i
    steps = 0
    while steps < noe:
        curr =  ranks[type_list[pos]]
        lefts[i][curr] = min(lefts[i][curr], steps)
        steps += 1
        pos = (pos - 1 + noe) % noe

for i in range(noq):
    froms, types, direction = [x for x in input().split()]
    froms, types = int(froms), int(types)
    ans = -1
    if direction == "R":
        print(rights[froms][types])
    else:
        print(lefts[froms][types])

