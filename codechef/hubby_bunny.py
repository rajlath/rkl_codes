'''
if ( Math.sqrt( ( x2-x1 ) * ( x2-x1 )  + ( y2-y1 ) * ( y2-y1 ) ) < ( radius1 + radius2 ) )

3
10 10 3
10 6 1
8 8 3
8 4 2
7 5 2
4 9 2
Output:
tangential
overlapping
not overlapping
'''

for _ in range(int(input())):
    x1, y1, r1 = [int(x) for x in input().split()]
    x2, y2, r2 = [int(x) for x in input().split()]
    dx = x2 - x1
    dy = y2 - y1
    dr = r1 + r2
    a  = dx * dx
    b  = dy * dy
    r  = dr * dr
    if a + b < r:
        print("overlapping")
    elif a + b == r:
        print("tangential")
    else:
        print("not overlapping")


