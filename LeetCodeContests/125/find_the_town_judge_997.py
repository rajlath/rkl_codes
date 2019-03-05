
from collections import defaultdict
class Solution:
    def findJudge(self, N, trust):
        if len(trust) == 0:return -1
        trusted = {}
        trusting = defaultdict(list)
        for i, v in enumerate(trust):
            a, b = v
            trusted[b] = trusted.get(b, 0) + 1
            trusting[a].append(b)
        #print(trusted, trusting)
        for k, v in trusted.items():
            if v == N - 1 and k not in trusting:
                return k
        return -1

print(Solution().findJudge(3, [[1,3],[2,3]]))

from collections import Counter

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_degree = Counter([b for a, b in trust])
        out_degree = Counter([a for a, b in trust])
        ok = []
        for x in range(1, N + 1):
            if in_degree[x] == N - 1 and out_degree[x] == 0:
                ok.append(x)
        if len(ok) == 1:
            return ok[0]
        return -1

