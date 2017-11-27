def prime_seive(n):
    primes = [1] * (n+1)
    primes_index=[0,1]
    primes[0],primes[1], primes[2] = 0, 1, 1
    for i in range(2, n):
        if primes[i]==1:
            primes_index.append(i)
            x = i + i
            while x < n:
                primes[x] = 0
                x += i
    return primes,primes_index

a, b = prime_seive(200000)

