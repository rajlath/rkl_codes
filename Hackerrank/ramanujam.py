
primes   = [True] * 1000005
primes[0] = False
primes[1] = False
for i in range(2, 1000000):
    if primes[i]:
        j = i + i
        while j < 1000000:
            primes[j] = False
            j += i


valids = set()
for _ in range(int(input())):
    s = input()
    for i in range(len(s)):
        for j in range(i, len(s)):
            curr = s[i:j+1]
            if len(curr) <=6:
                if primes[int(curr)]:valids.add(s[i:j+1])
    print(len(valids))
