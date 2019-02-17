from itertools import accumulate
nb_liquid = int(input())
heights = [(0, 0)]
c = 0
h = 0
for _ in range(nb_liquid):
    p, hh = [int(x) for x in input().split()]
    for i in range(1, h+1):
        c += (p * 1)
        heights.append((i, c))
    h += hh
q = int(input())
for _ in range(q):
    l, r = [int(x) for x in input().split()]
    if r > 




