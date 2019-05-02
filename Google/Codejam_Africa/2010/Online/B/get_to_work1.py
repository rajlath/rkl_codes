# -*- coding: utf-8 -*-
import sys

fin = sys.stdin
C = int(fin.readline())
o = "outs_small_1.txt"
for case in range(1,C+1):
    N, T = map(int, fin.readline().split())
    T -= 1
    E = int(fin.readline())
    employees = [0]*N
    cars = [[] for i in range(N)]

    for i in range(E):
        H, P = map(int, fin.readline().split())
        H -= 1
        employees[H] += 1
        if P > 0:
            cars[H].append(P)
    #print employees
    #print cars
    for c in cars:
        c.sort()
        c.reverse()
    #print cars
    result = []
    for i in range(N):
        if i == T:
            result.append(0)
            continue
        rem = employees[i]
        used = 0
        for car in cars[i]:
            if rem <= 0:
                break
            rem -= car
            used += 1
        if rem > 0:
            result = None
            break
        result.append(used)

    if result is None:
        print( "Case #%d: IMPOSSIBLE" % (case))
    else:
        ans = "Case #%d: %s" % (case, ' '.join(map(str, result)))
        print( ans, file = outs)
