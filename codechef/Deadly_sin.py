from math import gcd
for i in range(int(input())):
    a, b = [int(x) for x in input().split()]
    print(gcd(a, b)*2)