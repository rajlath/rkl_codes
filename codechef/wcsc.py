def seive(n=int(10 ** 6 + 1)):
    primes = [False, False] + [True for _ in range(n-2)]
    curr = 2
    while curr * curr <= n:
        if primes[curr]:
            for mults in range(curr * curr, n, curr):
                primes[mults] = False
        curr += 1
    return primes

primes = seive()
nb_test = int(input())
for _ in range(nb_test):
    curr = int(input())
    if curr <= 3:print(-1)
    elif curr % 2 == 0: print(1)
    else :
        if primes[curr - 2]:
            print(1)
        else:
            print(2)


