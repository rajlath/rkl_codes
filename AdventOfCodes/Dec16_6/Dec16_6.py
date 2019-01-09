# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
from collections import defaultdict
#enter a comment here

def manhattan(x1,y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
    
    

lines = [x.strip() for x in open("input.txt").readlines()]
points= [list(map(int, (re.findall(r'\d+', x)))) for x in lines]
x0, x1 = min(x for x, y in points), max(x for x, y in points)
y0, y1 = min(y for x, y in points), max(y for x, y in points)
counts   = defaultdict(int)
infinite = set()
for y in range(y0, y1+1):
    for x in range(x0, x1+1):
        ds = sorted((manhattan(x, y, px, py), i) for i, (px, py) in enumerate(points))
        if ds[0][0] != ds[1][0]:
            counts[ds[0][1]] += 1
            if x == x0 or y == y0 or x == x1 or y == y1:
                infinite.add(ds[0][1])
for k in infinite:counts.pop(k)   
print(max(counts.values()))

# part 2
count = 0
# iterate over all cells in the bounding box
for y in range(y0, y1 + 1):
    for x in range(x0, x1 + 1):
        # sum up the distance to all points from this cell
        # increment our counter if the sum is less than 10000
        if sum(manhattan(x, y, px, py) for px, py in points) < 10000:
            count += 1
print(count)             
        