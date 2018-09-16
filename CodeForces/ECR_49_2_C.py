'''
3
4
7 2 2 7
8
2 8 1 4 8 2 1 5
5
5 5 5 5 5
'''
from collections import Counter

for i in range(int(input())):
    candidates = []
    lens = int(input())
    sticks= [int(x) for x in input().split()]
    sticks = sorted(sticks)
    #print(sticks)
    i = 0
    while i < lens-1:
        if sticks[i] == sticks[i+1]:
            candidates.append(sticks[i])
            i += 2
        else:
            i += 1
    candidates = sorted(candidates)
    print(candidates[0], candidates[0], candidates[1], candidates[1])

