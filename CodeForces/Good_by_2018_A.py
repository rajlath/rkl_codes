y, b, r = [int(x) for x in input().split()]
for i in range(y, 0, -1):
    if i + 1 <= b and i + 2 <= r:
        print(3 * i + 3)
        break

