'''
inputCopy
6 60
0 0
1 20
3 21
5 0
19 30
23 40
outputCopy
6 1
inputCopy
16 50
0 30
1 20
3 0
4 30
6 10
7 50
9 30
11 10
12 50
14 30
16 10
17 50
19 30
21 10
22 50
23 59
outputCopy
24 50
inputCopy
3 17
0 30
1 0
12 0
outputCopy
0 0
'''
minutes = [0] * 2400
nol, gap = [int(x) for x in input().split()]
hh, mm = [int(x) for x in input().split()]
last_land = hh * 60 + mm
for i in range(1, nol):
    hh, mm = [int(x) for x in input().split()]
    curr_land = hh * 60 + mm
    if abs(curr_land - last_land) >= gap * 2:
        print(hh+1, mm+1)
        break


