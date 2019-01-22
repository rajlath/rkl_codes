'''
2
6
5 3 1 4 3 2
4 3 1 1 1 5
5
1 2 3 4 5
5 4 3 2 1

10
7
5 9 3 0 1 5 2
2 2 4 0 6 1 8
2
3 9
7 0
7
6 2 2 6 4 3 9
2 9 7 7 0 1 1
4
9 4 9 0
8 4 0 5
8
4 5 5 0 5 6 7 3
0 4 6 0 2 2 8 4
7
9 9 8 0 1 5 1
4 7 2 5 1 2 1
8
1 0 8 5 3 0 9 2
2 9 0 8 8 7 1 5
5
4 7 3 5 0
5 6 8 5 2
5
5 3 0 8 8
7 2 0 6 9
2
2 5
6 9

Rupam
Rupam
Rupam
Rupam
Rupam
Rupam
Ankit
Ankit
Rupam
Ankit

Rupam
Rupam
Ankit
Rupam
Rupam
Rupam
Ankit
Rupam
Ankit
Ankit

'''
def get_max_weight(a):
    rmax = -1
    rw   = -1
    for i in a.keys():
        if a[i] > rmax:
            rw = i
            rmax = a[i]
        else:
            if a[i] == rmax:
                if i > rw:
                    rmax = a[i]
                    rw = i
    return rw

from collections import Counter
for _ in range(int(input())):
    noe = int(input())
    rupam = dict(Counter([int(x) for x in input().split()]))
    ankit = dict(Counter([int(x) for x in input().split()]))
    rw = get_max_weight(rupam)
    aw = get_max_weight(ankit)
    if rw == aw:print("Tie")
    elif rw > aw:print("Rupam")
    else:print("Ankit")










