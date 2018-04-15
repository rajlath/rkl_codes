def seive(n):
    primes = [1]*(n+10)
    for i in range(2,n+10):
        if primes[i]:
            for j in range(2*i, n+10,i):
                primes[j]=0
    return primes

primes = seive(10**6 + 10)
for _ in range(int(input())):
    l, r = [int(x) for x in input().split()]
    for x in range(l, r+1):
        if primes[x]:
            break
    if x == r:
        print("0")
        continue
    else:
        for y in range(r, l-1, -1):
            if primes[y]:
                break
    print(y-x)



