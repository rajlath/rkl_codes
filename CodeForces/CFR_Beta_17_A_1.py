primes = []
n, k = [int(x) for x in input().split()]
for x in range(2, n+1):
    if all((x % p != 0 for p in primes)):
        primes += [x]
for x in range(len(primes) - 1):
    if primes[x] + primes[x+1] + 1 in primes:
        k -= 1
print(["No", "Yes"][k<=0])


