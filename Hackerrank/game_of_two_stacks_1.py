'''
lenA, lenB, sum_needed = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

sums = 0
cache=[]

while sums <= sum_needed:
    cache.append(A.pop(0))
    sums += cache[-1]

count = len(cache)
max_now = count
score = 0
for i in range(lenB):
    score += B.pop(0)
    count += 1
    while score > sum_needed and count > 0 and len(cache) >0:
        count -= 1
        score -= cache.pop()
    if score <= sum_needed  and count > max_now:
        max_now = count
print(max_now)
'''
import bisect
from itertools import accumulate
for _ in range(int(input())):
    lA, lB, X = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    AC = [0] + list(accumulate(A))
    BC = [0] + list(accumulate(B))

    ans = 0
    for i, x in enumerate(AC):
        if x > X:break
        j = bisect.bisect(BC, X-x)
        if j >= 0:
            ans = max(ans, i+j-1)
    print(ans)

'''
from sys import stdin
rr = lambda: stdin.readline().strip()
rrm = lambda: map(int, rr().split())

import bisect
def solve(X, A, B):
    Pa, Pb = [0], [0]
    for x in A:
        Pa.append(Pa[-1] + x)
    for x in B:
        Pb.append(Pb[-1] + x)
    print(Pa, Pb)
    ans = 0
    #Pa[i] + Pb[j] <= X means a score of i+j
    for i, x in enumerate(Pa):
        if x > X: break
        j = bisect.bisect(Pb, X-x)
        if j >= 0:
            ans = max(ans, i + j - 1)
    return ans

for _ in xrange(int(rr())):
    print solve(rrm()[2], rrm(), rrm())
'''






