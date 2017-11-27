def gcd(a, b):
    '''
    find gcd of two numbers
    a : int
    b : int
    ret int
    '''
    if b == 0:return a
    else:
        return gcd(b, a%b)


def gcd1(a, b):
    '''
    find gcd of two numbers
    non-recursive
    a : int
    b : int
    ret int
    '''
    while b:
        a %= b
        a, b = b, a
    return a

def xgcd(b, n):
    '''
    extended gcd
    iterative
    algorithm to compute integers x and y such that
        ax + by = gcd(a, b)
    int a
    int b
    returns int:gcd, int:x, int y
    '''
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

import sys
sys.setrecursionlimit(1000000)
# long type,32bit OS 4B,64bit OS 8B(1bit for sign)


def egcd(a, b):
    '''
    return (g, x, y)
    a*x + b*y = gcd(x, y)
    int a
    int b
    ret g x y all integers
    recursive method
    '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    '''
    modular inverse
    x = mulinv(b) mod n, (x * b) % n == 1
    An application of extended GCD algorithm to finding modular inverses:
    b int
    n int
    if both primes
    ret int
    else None
    '''
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


def lcm(a, b):
    '''
    find lcm of two numbers
    a  : int
    b  : int
    ret int
    requires gcd function
    '''
    return  a * b // gcd(a, b)

print(gcd(12, 32))   #4
print(gcd1(12, 32))  #4
print(xgcd(12, 32))  # 4 3 -1
print(lcm(12, 32))   #96
print(mulinv(2, 23))


