
# -*- coding: utf-8 -*-
# @Date    : 2018-09-24 09:24:59
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    :
# @Version : 1.0.0

from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

'''
Sample Input:
2
15
3
Sample Output:
47
5
'''
N = 15485864
def sieve():
    primes = [1] * (N+1)
    i = 2
    while (i* i) < N:
        if primes[i]:
            try:
                j = i * 2
                while j <= N:
                    primes[j] = 0
                    j += i
            except IndexError:
                print
        i += 1
    return primes

prime = sieve()
primes = [x for x in range(2, N) if prime[x]]
nb_test = read_int()
for _ in range(nb_test):
    print(primes[read_int()-1])

