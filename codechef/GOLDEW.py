def rwh_primes1(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

nol = int(input())
arr = [int(x) for x in input().split()]
n   = max(arr)
primes = rwh_primes1(n+1)
for i in range(nol):
    curr = arr[i]
    valid= []
    if curr %2 == 0 and curr not in primes:
        for j in primes:
            if  j < curr:
                curr1 = curr - j
                if curr1 in primes:
                    ans = curr1 * j
                    valid.append(ans)
            else:
                break
    if len(valid)==0:
            print(0, end=" ")
    else:
        print(min(valid), end=" ")





