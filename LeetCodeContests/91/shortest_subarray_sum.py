from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        ps = [0]
        for x in A:
            ps.append(x + ps[-1])
        maxs = len(ps)
        ans  = maxs
        q =    []
        for i in range(len(ps)):
            #print(q)
            while q and ps[i] - ps[q[0]] >= K:
                ans = min(ans, i - q[0])
                q.pop(0)
            while q and ps[i] <= ps[q[-1]]:
                q.pop()
            q.append(i)
        return -1 if ans == maxs else ans
sol = Solution()
print(sol.shortestSubarray([1, 2], 4))