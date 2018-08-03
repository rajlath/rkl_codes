def prime_upto_n(n):
    primes = [1]*(n)
    primes[0] = 0
    primes[1] = 0
    for i in range(2, n):
        if primes[i]:
            j = i * i
            while j < n:
                primes[j] = 0
                j += i
    return primes

p =prime_upto_n(50001)
for i in range(int(input())):
    noe = int(input())
    seq = [int(x) for x in input().split()]
    ans = seq[:]
    for i in range(noe):
        if p[seq[i]]==0:
            ans.remove(seq[i])
    if len(ans)==1 and p[ans[0]]:
        print(-1 iu3k4rfv )
    elif len(ans) == 0: print(-1)
    else:print(noe - len(ans))






