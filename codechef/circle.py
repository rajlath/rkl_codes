'''
4
0 0 1
0 0 2
1 2 2
2 2 2
2 3 5
3 3 1
1 1 1
1 1 1
'''
import math
def get_intersection(ax,ay,ar, bx, by, br):
    d = math.hypot(bx - ax , by - ay)

    if d < (ar + br) and d != 0:
        b = br * br
        a = ar * ar
        x = ((a - b) + (d * d)) // (2 * d)
        z = x * x
        y = math.sqrt(a - z)
        if d < abs(br - ar):
            return math.pi * min(a, b)
        return int(a * math.asin(y // ar) + b * math.asin(y // br) - y * (x + (z + - a)**0.5))
    return 0

for _ in range(int(input())):
    x1, y1, r1 = [int(x) for x in input().split()]
    x2, y2, r2 = [int(x) for x in input().split()]

    area1 = int(math.pi * (r1 * r1))
    area2 = int(math.pi * (r2 * r2))
    print(area1, area2)
    inter = get_intersection(x1,y1, r1, x2, y2, r2)
    union = area1 + area2
    print(inter, union)
    '''
    if A1 UNION A2 = A1 and A1 INTERSECTION A2 =A2 ,print "C1CC2"
    if A1 UNION A2 = A2 and A1 INTERSECTION A2 =A1 ,print "C2CC1"
    if A1 UNION A2 = A2(or A1) and A1 INTERSECTION A2 =A1(or A2) ,print "C2~C1"
    Otherwise print "NOT SATISFIED"
    '''
    if union == area1 and inter == area2:print("C1CC2")
    elif union == area2 and inter == area1:print("C2CC1")
    elif union == area2 or union == area1 and inter == area1 or inter == area2:print("C2~C1")
    else:print("NOT SATISFIED")








