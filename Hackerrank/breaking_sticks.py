#!/bin/python3

import sys

def get_primes(n): # Get all primes less than or equal to n in order
    is_prime = [True] * (n + 1)
    rtn = []
    for i in range(2, n + 1):
        if not is_prime[i]: continue
        rtn.append(i)
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1
    return rtn

def longestSequence(a):
    #  Return the length of the longest possible sequence of moves.
    cache = dict() # cache[n] stores the minimum number of moves required to eat up n
    primes = get_primes(1000000)
    def get_cache(n):
        if n == 0: return 0
        if n == 1: return 1
        if n in cache: return cache[n]
        best_p = n
        for p in primes:
            if p >= n: break
            elif n % p == 0:
                best_p = p
                break
        #rtn = get_cache(n // best_p) * best_p + 1
        rtn = n + get_cache(n // best_p)
        cache[n] = rtn
        return rtn
    if not a: return 0
    else:
        results = [get_cache(n) for n in a]
        return sum(results)

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = longestSequence(a)
    print(result)