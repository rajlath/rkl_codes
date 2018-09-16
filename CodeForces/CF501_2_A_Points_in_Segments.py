'''
A. Points in Segments

You are given a set of n segments on the axis Ox , each segment has integer endpoints between 1  and m
inclusive. Segments may intersect, overlap or even coincide with each other. Each segment is characterized by
two integers l i and r i  (1 ≤ li≤ri≤m) — coordinates of the left and of the right endpoints.
Consider all integer points between1 andm inclusive. Your task is to print all such points that don't belong to any segment.
The point xbelongs to the segment l ;r] if and only if l ≤ x ≤ r.

Input
The first line of the input contains two integers
n  and m  ( 1≤ n , m≤100) — the number of segments and the upper bound for coordinates.

The next nlines contain two integers each l i and r i (1≤li≤ri≤m) — the endpoints of thei-th segment.
Segments may intersect, overlap or even coincide with each other.
Note, it is possible that li=ri, i.e. a segment can degenerate to a point.

Output
In the first line print one integer k — the number of points that don't belong to any segment.
In the second line print exactly k integers in any order — the points that don't belong to any segment.
All points you print should be distinct.

If there are no such points at all, print a single integer 0
in the first line and either leave the second line empty or do not print it at all.

Examples
inputCopy
3 5
2 2
1 2
5 5
outputCopy
2
3 4
inputCopy
1 7
1 7
outputCopy
0

Note
In the first example the point 1 belongs to the second segment, the point 2 belongs to the first and
the second segments and the point 5 belongs to the third segment. The points 3  and 4
do not belong to any segment.
In the second example all the points from 1 to 7 belong to the first segment.
'''
import datetime
#Solution 1 0:00:07.848164
'''
start = datetime.datetime.now()
nos, maxp = [int(x) for x in input().split()]
points    = {i:0 for i in range(1, maxp+1)}
for i in range(nos):
    a, b = [int(x) for x in input().split()]
    for i in range(a, b+1):points[i] = 1
ans = [k for k, v in points.items() if points[k]==0]
print(len(ans))
print(*sorted(ans))
print(datetime.datetime.now() - start)

#solution 2 (n + m ) solution
'''
#start = datetime.datetime.now()
nos, maxp = [int(x) for x in input().split()]
points = [0] * (maxp+2)
for i in range(nos):
    l, r = [int(x) for x in input().split()]
    points[l-1] += 1
    points[r] -= 1

print(points)
ans = [i for i in range(1, maxp+1) if points[i] == 0]
print(len(ans))
print(*ans)
#print(datetime.datetime.now() - start)

#solution 3  n * m solution
'''
start = datetime.datetime.now()
nos, maxp = [int(x) for x in input().split()]
points = [list([int(x) for x in input().split()]) for _ in range(nos)]
def invalid(x):
    for i in range(nos):
        if points[i][0] <= x and x <= points[i][1]:return False
    return True
ans = list(filter(invalid, [i for i in range(1, maxp+1)]))
print(len(ans))
print(*ans)
print(datetime.datetime.now() - start)
'''


