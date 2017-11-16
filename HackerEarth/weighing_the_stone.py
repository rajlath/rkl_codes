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
from collections import Counter
for _ in range(int(input())):
    noe = int(input())
    rupam = Counter([int(x) for x in input().split()])
    ankit = Counter([int(x) for x in input().split()])
    rc    = rupam.most_common()
    ac    = ankit.most_common()
    
    rmx   = rc[0][1]
    amx   = ac[0][1]
    rx    = rc[0][0]
    ax    = rc[0][0]
    
    for k, v in rc:
        if v == rmx:
            rx = max(rx, k)
        else:
            break
    for k, v in ac:
        if v == amx:
            ax = max(ax, k)
        else:
            break 
        
    if rx == ax:print("Tie")               
    elif rx> ax:print("Rupam")
    else:print("Ankit")
    
