'''
Input:
2
2 3
8 24

Output:
6
24
'''
from math import gcd
def lcm(x, y):
     lcm = (x*y)//gcd(x,y)
     return lcm
for _ in range(int(input())):
    a, b = [int(x) for x in input().strip().split()]
    print(lcm(a, b))

