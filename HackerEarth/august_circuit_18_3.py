def prime_seive(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for i in range(2, n+1):
        if primes[i]:
            j = i+i
            while j < (n+1):
                primes[j] = False
                j += i
    return primes

primes = prime_seive(1001)
noe = int(input())
arr = [int(x) for x in input().split()]
k   = int(input())
segmets = []
last = 0
sums = 0
for i, v in enumerate(arr):
    if v == 1:
        segmets.append(arr[i:i+1])
        if last - i >0:
            segmets.append(arr[last:i])
        last = i+ 1
        k -= 1
        if k == 0:
            segmets.append(arr[i+1:])
            break
    else:
        print(last)
        seg = []
        sums += v
        if primes[sums] and k > 1:
            seg.append(v)

            last = i+1
            k -= 1
        if k == 0:
            segmets.append(arr[i+1:])
            break
print(segmets)



