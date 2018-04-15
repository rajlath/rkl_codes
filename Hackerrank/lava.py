'''
c =[[0 for x in range(300)] for y in range(300)]

n = int(input())
maxs = 0
for _ in range(int(input())):
    x, y, w = [int(x) for x in input().split()]
    for i in range(n):
        for j in range(n):
            dx = abs(i-x)
            dy = abs(j-y)
            c[i][j] += max(0, w - max(dx, dy))
            #maxs = max(maxs, c[i][j])
print(max(list(map(max, c))))
print(maxs)
'''
#!/bin/python3

import sys


def caculateEffect(effects, x, y):
    total = 0
    for x_e, y_e, w in effects:
        dist = max(abs(x - x_e), abs(y - y_e))
        if dist < w:
            total += w - dist
    return total

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())

    effects = list()

    for a0 in range(m):
        x, y, w = input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]
        effects.append((x, y, w))

    maxScore = 0

    for x in range(n):
        for y in range(n):
            eff = caculateEffect(effects, x, y)
            maxScore = max(maxScore, eff)

    print(maxScore)

