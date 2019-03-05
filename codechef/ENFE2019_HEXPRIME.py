def seive(N):
    primes = [False, False] + [True] * (N+5)
    seives = []
    for i in range(2, N+5):
        if primes[i]:
            seives.append(i)
            j = i + i
            while j < (N+5):
                primes[j] = False
                j += i
    return seives



prime = seive(10 ** 5)
valids = []
for i in prime:
    if i + 6 in prime:
        valids.append(i)
nb_test = int(input())
for _ in range(nb_test):
    ub = int(input())
    cnt = 0
    for i in valids:
        if i > ub:
            break
        cnt += 1
    print(cnt)


