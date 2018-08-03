limit = 10 ** 6 + 1
primes = [False, False] + [True] * limit
p = 2
while p * p <= limit:
    for i in range(p*2, limit, p):
        primes[i] = False
    p += 1
prime_number = [i for i, v in enumerate(primes) if v]
prime_factor = [0] * limit
for prime in prime_number:
    for j in range(prime, limit, prime):
        prime_factor[j] += 1

for _ in range(int(input())):
    n, m = [int(x) for x in input().split()]
    print(sum(prime_factor[n:m]))





