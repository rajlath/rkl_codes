
N = 1000010
primes = [1] * N
for i in range(2, N):
    if 1 == primes[i]:
        for j in range(i * i, N, i):
            primes[j] = 2
n = int(input())
ans = primes[2:n+2]
print(len(set(ans)))
print(*ans)


