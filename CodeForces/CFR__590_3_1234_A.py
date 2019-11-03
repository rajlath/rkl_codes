from math import ceil
for _ in range(int(input())):
    lens = int(input())
    vals = [int(x) for x in input().split()]
    print(ceil(sum(vals)/lens))