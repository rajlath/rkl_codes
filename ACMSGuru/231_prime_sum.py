N = 1000000
primes = [True] * (N+1)
primes[0] = False
primes[1] = False
n = int(input())
i = 2
while i*i < (n+1):
    for i in range(2, N+1):
        if primes[i]:
            j = i * i
            while j < N+1:
                primes[j] = False
                j += 1


ans=[]
for i in range(5, n):
    if primes[i-2] and primes[i]:
        ans.append(primes[i-2])
print(len(ans))
for i in range(len(ans)):
    print("{} {}".format(2, ans[i]))
