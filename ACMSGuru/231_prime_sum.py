def sieve(n):
    maxn = (n
    '\
    huj]'h * 10 + 100
    Size = n
    prime = [0] * Size
    prime[0] = 2
    cnt = 1
    mark = [False] * maxn
    for i in xrange(3, n + 1, 2):
        if not mark[i]:
            prime[cnt] = i
            cnt += 1
        j = 1
        while j < cnt and  prime[j] <= n // i:
            mark[i*prime[j]] = 1
            if( not (i%prime[j])): break
            j +=1
    return prime, cnt

n = int(input())
primes, cnt = sieve(n)
ans = []
for i in xrange(1, cnt):
    if primes[i] - primes[i-1] == 2:
        ans.append(i-1)
print(len(ans))
for i in xrange(len(ans)):
    print("{} {}".format(2, primes[ans[i]]))


