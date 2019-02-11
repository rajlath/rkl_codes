def seive(n):
    prime = [False, False] + [True] * (n)
    primes = []
    for i in range(2, n+1):
        if prime[i] == True:
            primes.append(i)
            j = i * i
            while j < (n+1):
                prime[j] = False
                j += i
    return primes

primes_all = seive(8000)
valid = []
for i in range(len(primes_all)-1):
    valid.append(primes_all[i] + primes_all[i+1] + 1)
number, at_least = [int(x) for x in input().split()]
i = 0
for j in primes_all:
    if j <= number:
        i += 1
    else:
        break
print(["No", "Yes"][i>=at_least])