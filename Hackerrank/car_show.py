
#solved by AWice

import collections

rrm = lambda: map(int, raw_input().split())
N, Q = rrm()
A = rrm()
queries = [rrm() for _ in xrange(Q)]
prev = []
left = 0
count = [0] * (10**6 + 1)
dupes = 0
for right, x in enumerate(A):
    count[x] += 1
    if count[x] == 2: dupes += 1
    while dupes:
        count[A[left]] -= 1
        if count[A[left]] == 1: dupes -= 1
        left += 1
    prev.append(left)

P = [0]
for x in prev:
    P.append(P[-1] + x)

#P[x] = sum(prev[:x])
import bisect
def query(L, R):
    #want sum max(L, prev[x]) for x = L...R
    j = ix = bisect.bisect(prev, L)
    for i in (ix-1, ix, ix+1):
        if 0 <= i < len(prev) and prev[i] <= L: j = i

    #For indices above j, the answer is prev[ix]
    #Indices at or below, answer is L
    if j > R: return L * (R-L+1)
    if j < L: return P[R+1]-P[L]
    #print 'yo', prev, 'j', j, 'LR', L, R
    ans = P[R+1] - P[j+1]
    ans += (j - L + 1) * L
    return ans

for L, R in queries:
    L-=1;R-=1
    ans = R*(R+1)/2 - L*(L-1)/2 + R-L+1
    print ans - query(L, R)