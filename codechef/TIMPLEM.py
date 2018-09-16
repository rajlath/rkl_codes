
'''
def power(base, exp):
    if exp < 0:
        return 1 // power(base, -exp)
    ans = 1
    while exp:
        if exp & 1:
            ans *= base
        exp >>= 1
        base *= base
    return ans

def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def prime_seive(n):
    primes = [0,0] + [1]*(N-2)
    DP     = [0] * N
    for i in range(2, n):
        if primes[i]:
            DP[i] = pow(i, i, mod)
            DP[i] = DP[i] + DP[i-1]
            for j in range(i+i, n, i):
                primes[i] = 0
        else:
            DP[i] = DP[i-1]
    return DP
'''
from math import sqrt
N = 100001
mod  = 1000000007

def seive(n):
    global DP
    primes = [0, 0] + [1] * N
    for i in range(2,n):
        if primes[i]==1:
            DP[i] = pow(i, i, mod)
            DP[i] += DP[i-1]
            for j in range(i+i,n,i):
                primes[j]=0
        else:
            DP[i] = DP[i-1]
    return primes


DP     = [0] * N
primes = seive(N)
for i in range(2, N):
    if primes[i]:
        DP[i] = pow(i, i, mod)
        DP[i] += DP[i-1]
    else:
        DP[i] = DP[i-1]
t = int(input())
for i in range(t):
    l, r = [int(x) for x in input().split()]
    print( (DP[r] - DP[l-1]) % mod)

