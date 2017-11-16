'''
SAMPLE INPUT 
5
1 1
2 1
1 3
1 1
1 3
SAMPLE OUTPUT 
1 1 2
1 3 2
2 1 1
'''
points = {}
for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    points[(a, b)] = points.get((a, b), 0) + 1
p = sorted(points)    
for x in p:
    print(x[0],x[1],points[x])

