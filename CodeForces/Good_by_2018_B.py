nb_points = int(input())
sum_x = 0
sum_y = 0
for _ in range(2 * nb_points):
    a, b = [int(x) for x in input().split()]
    sum_x += a
    sum_y += b
print(sum_x//nb_points, sum_y//nb_points)