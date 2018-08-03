def seive(n):
    primes = [False, False] + [True] * n
    for i in range(2, n):
        if primes[i]:
            for j in range(i*i, n, i):primes[j] = False
    return  primes

n = int(input())
prime = seive(n)
ans = [2]
for i in range(5, n):
    if prime[i-2] and prime[i]:
        ans.append(i-2)
if n < 5:
    print(0)
else:
    print(len(ans))
    print(*ans)


