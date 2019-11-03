from math import sqrt

def is_power(n):
    for i in range(1, int(sqrt(n) + 1)):
        if i * i == n:
            return True
    return False
lens = int(input())
vals = [int(x) for x in input().split()]
for i in vals:
    print(["No", "Yes"][is_power(i)], end=" ")