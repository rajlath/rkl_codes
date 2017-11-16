from itertools import product
a, b = [int(x) for x in input().split()]
x1 = [int(x) for x in input().split()]
y1 = [int(x) for x in input().split()]

minx = min(x1)
miny = min(y1)
if minx == miny : print(minx)
else:
    if minx > miny:
        print(int(miny)*10 + minx)
    else:
        print(minx * 10 + miny)    
