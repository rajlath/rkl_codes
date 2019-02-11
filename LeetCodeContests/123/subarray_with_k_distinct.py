from collections import defaultdict
class Tracker:
    def __init__(self):
        self.c = defaultdict(int)
        self.n = 0
    def __len__(self):
        return self.n
    def add(self, x):
        if self.c[x] == 0: self.n += 1
        self.c[x] += 1
    def remove(self, x):
        self.c[x] -= 1
        if self.c[x] == 0: self.n -= 1

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        j0 = j1 = 0
        t0 = Tracker()
        t1 = Tracker()
        n = len(A)
        r = 0
        for i in xrange(n):
            while j0 < n and len(t0) < K:
                t0.add(A[j0])
                j0 += 1
            while j1 < n and len(t1) < K+1:
                t1.add(A[j1])
                j1 += 1
            if len(t0) < K: break
            if len(t1) < K + 1: j1 = n+1
            r += j1 - j0
            t0.remove(A[i])
            t1.remove(A[i])
        return r