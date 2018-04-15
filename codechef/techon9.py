def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

primes = sieve_for_primes_to(int(10e7+10))

for _ in range(int(input())):
    n = int(input())
    for x in primes:
        if x <= n:
            if str(x) == str(x)[::-1]:
                print(x, end=" ")
        else:
            break