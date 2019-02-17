def sieve(limit):
    if limit < 2: return []
    factors = set()
    primes  = [2,]
    for i in range(3, limit+1, 2):
        if i not in factors:
            primes.append(i)
            factors.update(range(i ** 2, limit, i))
    return primes

#print(sieve(1))