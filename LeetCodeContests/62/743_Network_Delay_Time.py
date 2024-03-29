'''
743. Network Delay Time My SubmissionsBack to Contest
Difficulty: Medium
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node,
v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K.
How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
'''
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        maxs = 10e9
        a = [maxs] * (N+1)
        a[K] = 0
        for i in range(N):
            for j in range(len(times)):
                v, u, t = tuple(times[j])
                if a[v] + t < a[u]:
                    a[u] = a[v] +t
        ans = 0
        for i in range(1, N+1):
            ans = max(ans, a[i])
        return [-1, ans][ans!=maxs]

sol = Solution()
print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))



