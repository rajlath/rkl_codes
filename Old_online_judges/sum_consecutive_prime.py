'''
Source: ACM Japan 2005.
IDs for online judges: POJ 2739, UVA 3399.

Some positive integers can be arrived at by adding consecutive primes.
Ex.
53 5 + 7 + 11 + 13 + 17 and 53
41 2 + 3 + 5 + 7 + 11 + 13, 11 + 13 + 17, and 41
3  3
but not
20 3 + 5 + 5 + 7  // 5 is repeated and hence not consecutive

Task
Write a program that reports the number of representations for the given positive integer.

Input
The input is a sequence of positive integers, each in a separate line. The integers are between 2 and
10,000, inclusive. The end of the input is indicated by a zero

output
For each input write how many prime representation it has

constraints
None of the representation will have a prime number greater then 10000

methodology
1.create a prime sieve upto 10000
2.Starting with first prime
  2a. keep adding next primes till either its equal to input or exceed
  2b. if equal we have the number
  2c. if exceed: start again with above loop using next prime number
  2d. ultimately if prime number at (2) exceed input
      it can not have a prime representation

result: Time limit exceed.
option: Try some other faster supported language like Java or c++
        accepted solution prime_expression.cpp
        
'''
from sys import stdin, stdout

def prime_seive(n):
    primes_index = [1]*(n+1)
    primes = []
    for i in range(2, n+1):
        if primes_index[i]:
            primes.append(i)
            x = i + i
            while x < n:
                primes_index[x] = 0
                x += i
    return primes

primes = prime_seive(10001)
inps = 1
while inps != 0:
    inps = int(stdin.readline().strip())
    cnt  = 0
    for i in range(len(primes)):
        if i > inps:break
        sums = 0
        for j in range(i,len(primes)):
            sums += primes[j]
            if sums == inps:
                cnt += 1
                break
    if inps > 0:print(cnt)











