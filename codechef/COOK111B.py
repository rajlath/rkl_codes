from math import log
nb = int(input())
for _ in range(nb):
    curr = int(input())
    zeros = 0
    while curr % 10 == 0:
        zeros += 1
        curr //= 10
    x = log(curr, 2)
    print(["No", "Yes"][x==int(x) and zeros >= x])