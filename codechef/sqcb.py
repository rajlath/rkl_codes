import math
def cbrt(n) :
    return (int)( n ** (1. / 3))

def CountCubes(a, b) :
    cnt = 0
    acrt = cbrt(a)
    bcrt = cbrt(b)
    for i in xrange(acrt, bcrt + 1) :
        if (i * i * i >= a and i * i * i <= b) :
            cnt += 1
    return cnt
def CountSquares(a, b):
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

from sys import stdin
nots = int(stdin.readline())
for _ in xrange(nots):
    n = int(stdin.readline())
    ans = CountCubes(1, n+1) + CountSquares(1, n+1)
    x = 1
    y = 1
    while x <= n+1:
        ans -= 1
        y += 1
        x = pow(y, 6)
        #print(x)
    print(int(ans))