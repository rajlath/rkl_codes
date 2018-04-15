'''
10
18 15
16 11
13 12
19 17
16 13
16 18
17 11
18 13
20 18
16 11
4
2
4
1
2
3
1
6
3
2
'''
def seive(n):
    primes = [1]*(n+10)
    for i in range(2,n+10):
        if primes[i]:
            for j in range(2*i, n+10,i):
                primes[j]=0
    return primes

n = 1000000

#primes = seive(n)
'''
def is_prime(num):
    if num % 2 == 0 and num != 2 or num <= 1:
        return False
    for i in range(3, int(num ** (0.5)) + 1, 2):
        if num % i == 0:
            return False
    return True
'''
primes = seive(n)
for _ in range(int(input())):
    a, b = sorted([int(x) for x in input().split()])
    ab = a + b + 1
    while True:
        if primes[ab]:
            print(ab - a - b)
            break
        else:ab+=1

