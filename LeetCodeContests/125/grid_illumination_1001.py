import collections
import bisect

class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = N
        row = collections.Counter()
        col = collections.Counter()
        ldiag = collections.Counter()
        rdiag = collections.Counter()
        for x, y in lamps:
            row[x] += 1
            col[y] += 1
            ldiag[x - y] += 1
            rdiag[x + y] += 1

        mark = {}
        for x, y in lamps:
            if x not in mark:
                mark[x] = []
            bisect.insort(mark[x], y)

        ans = []
        erase = set([])
        for x, y in queries:
            if any([row[x] > 0, col[y] > 0, ldiag[x - y] > 0, rdiag[x + y] > 0]):
                ans.append(1)
            else:
                ans.append(0)

            for i in [x - 1, x, x + 1]:
                if i < 0 or x >= n:
                    continue
                if i not in mark:
                    continue

                p = bisect.bisect_left(mark[i], y - 1)
                q = bisect.bisect_right(mark[i], y + 1)
                for k in range(p, q):
                    j = mark[i][k]
                    if (i, j) in erase:
                        continue
                    row[i] -= 1
                    col[j] -= 1
                    ldiag[i - j] -= 1
                    rdiag[i + j] -= 1
                    erase.add((i, j))
        return ans