primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
curr, nexts = [int(x) for x in input().split()]
if primes[primes.index(curr) + 1] == nexts:
    print("YES")
else:
    print("NO")
