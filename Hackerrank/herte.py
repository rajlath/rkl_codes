'''
1 1
1 2
2 2
2 3
3 3
1 11
2 20
999000000 1000000000
1 1000001
2 1000002

0
0
0
1
0
4
7
0
78497
78497
'''
maxs  = 100000
prefix = [0] * maxs
primes = [True] * maxs
def count_primes():
    p = 2
    while p * p < maxs:
        if primes[p]:
            i = p * 2
            while i < maxs:
                primes[i] = False
                i += p
        p += 1
count_primes()
for p in range(2, maxs):
    prefix[p] = prefix[p-1]
    if primes[p] : prefix[p] += 1
print(primes[1:11])
for _ in range(int(input())):
    l, r = [int(x) for x in input().split()]
    if l <= 1: l = 2
    if l>=1 and r >= 1:
        ans = prefix[r] - prefix[l]
    else:
        ans = 0
    print(ans)


'''

    // Build prefix array
    prefix[0] = prefix[1] = 0;
    for (int p = 2; p <= MAX; p++) {
        prefix[p] = prefix[p - 1];
        if (prime[p])
            prefix[p]++;
    }
}
'''


