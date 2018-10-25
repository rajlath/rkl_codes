
# -*- coding: utf-8 -*-
# @Date    : 2018-10-13 07:32:39
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]




def Sieve(n):
    prime = [True for i in range(n+1)]
    prime[0], prime[1] = False, False
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    primes = []
    for i, v in enumerate(prime):
        if v:
            primes.append(i)
    return primes

def prime_factorization(n, primes):
    res = []
    for p in primes:
        while n%p == 0:
            res.append(p)
            n //= p
        if n <= 1:
            break
    return res


nb_test = read_int()
primes = Sieve(2000)
for _ in range(nb_test):
    n = read_int()
    nf= prime_factorization(n, primes)
    for i in range(len(nf)):
        for j in range()



