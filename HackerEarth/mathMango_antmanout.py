from functools import reduce
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
y = 1
for i in primes:
    y *= i
print(y)
fact = 784149080 // y
from itertools import compress

def primes(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2,*compress(range(3,n,2), sieve[1:])]

def factorization(n, primeslist):
    """ Returns a list of the prime factorization of n """
    pf = []
    for p in primeslist:
        if p*p > n : break
        count = 0
        while not n % p:
            n //= p
            count += 1
        if count > 0: pf.append((p, count))
    if n > 1: pf.append((n, 1))
    return pf

def divisors(n):
    """ Returns an unsorted list of the divisors of n """
    divs = [1]
    for p, e in factorization(n):
        divs += [x*p**k for k in range(1,e+1) for x in divs]
    return divs

n = y
primeslist = primes(int(n**0.5)+1)
print(divisors(n, primeslist))