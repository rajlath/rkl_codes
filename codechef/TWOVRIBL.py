from math import sqrt, floor
for _ in range(int(input())):
    given_x = int(input())
    x, y  = 0, 0
    count = 0
    for i in range(0, 100001):
        x = floor(sqrt(y)) + 1
        y += x * x
        if given_x < x:
            print(i)
            break
