
# -*- coding: utf-8 -*-
# @Date    : 2018-09-16 07:22:42
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]
def read_str_list(): return [x for x in stdin.readline().split().split()]


def is_prime_1(n):
    if n <= 1:return False
    i = 2
    while i * i <= n:
        if not n%i:return False
        i += 1
    return True

def seive(n):
    primes = [0, 0] + [1] * n
    i = 2
    while i * i <=  n:
        if primes[i]:
            j = 2 * i
            while j < n:
                primes[j] = 0
                j += i
        i += 1
    #return [x for x in range(122) if primes[x]]
    #return primes

def winner(s, maps):
    n1 = s[0]
    n2 = s[0:len(s)-1]
    win = False
    print(n1, n2)
    if not is_prime_1(int(n1)) and not winner(n1, maps):win = True
    if not is_prime_1(int(n2)) and not winner(n2, maps):win = True
    return win


nb_tests = read_int()
for _ in range(nb_tests):
    s = read_int()
    maps = {}
    if win(s//10) or win(s%10):
        print("Alice")
    else:
        print("Bob")
    
