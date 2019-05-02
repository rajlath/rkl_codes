def seive(n):
    composite = [False] * (n + 1)
    primes = []
    for i in range(2, n):
        if not composite[i]:
            primes.append(i)
        j = 0
        while j < len(primes) and i * primes[j] < n:
            composite[i * primes[j]] = True
            if i % primes[j] == 0:break
            j += 1
    return primes

prime = seive(10000000)
print(prime[:20])