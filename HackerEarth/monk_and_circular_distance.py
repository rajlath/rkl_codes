from math import hypot

def in_radius(c_x, c_y, r, x, y):
    return math.hypot(c_x-x, c_y-y) <= r

points = int(input())
all_points = []
for _ in range(points):
    all_points.append([int(x) for x in input().split()])
queries = int(input())
for i in range(int(input())):
    radius = 

