nb_points = int(input())
points = []
for _ in range(nb_points):
    x, y = [int(x) for x in input().split()]
    points.append((x, y))
valids = 0
for x, y in points:
    l = r = u = d = 0
    for x1, y1 in points:
        if y == y1:
            l += x < x1
            r += x > x1
        if x == x1:
            u += y < y1
            d += y > y1
    if l and r and u and d:valids += 1
print(valids)
