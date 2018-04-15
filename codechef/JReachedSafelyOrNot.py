'''
Input:
2
20 20
4 5
13
LLUUUUURRRRRR
10 10
3 4
7
UDUDDRR
'''
for _ in range(int(input())):
    m, n = [int(x) for x in input().split()]
    rx, ry = [int(x) for x in input().split()]
    nom  = int(input())
    moves= input()
    dx   = moves.count("L")*-1 + moves.count("R")
    dy   = moves.count("U") + moves.count("D")*-1

    if dx == rx and dy == ry:
        print("REACHED")
    elif dx < 0 or dx > m or dy < 0 or dy > n:
        print("DANGER")
    else:
        print("SOMEWHERE")

