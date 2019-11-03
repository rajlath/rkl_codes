from math import gcd
fav_number = int(input())
lens = int(input())
vals = [int(x) for x in input().split()]
print(sum([gcd(fav_number, x)==1 for x in vals]))
