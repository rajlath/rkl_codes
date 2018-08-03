from math import log, log10, log2
for _ in range(int(input())):
    x, y, a, b = [int(x) for x in input().split()]
    print([ "x^y","a^b"][y * log2(x) < b * log2(a)])
