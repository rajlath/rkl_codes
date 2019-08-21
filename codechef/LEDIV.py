from math import gcd,sqrt
LIMIT = 100001
lowest_prime = [i for i in range(LIMIT)]
for i in range(2, LIMIT):
    if lowest_prime[i] == i:
        for j in range(2 * i, LIMIT, i):
            lowest_prime[j] = min(lowest_prime[j], i)
for _ in range(int(input())):
    curr = int(input())
    arrs = [int(x) for x in input().split()]
    gc_d = 0
    for i in arrs:
        gc_d = gcd(gc_d, i)
    print(-1 if gc_d == 1 else lowest_prime[gc_d])
    
            
                    
                    