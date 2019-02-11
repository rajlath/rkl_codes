def squares_of_primes(n):
    primes = [False] * 2 + [True] * n
    primes_square = []
    for i in range(2, n+1):
        if primes[i]:
            primes_square.append(i * i)
            j = i + i
            while j < n:
                primes[j] = False
                j += i
    return primes_square

prime_square = squares_of_primes(1000500)
print(prime_square[:10])
while nb_test:
    curr = int(input())
    count = 0
    for i in prime_square:
        if i <= curr: count += 1
    print(count)
    nb_test -= 1

