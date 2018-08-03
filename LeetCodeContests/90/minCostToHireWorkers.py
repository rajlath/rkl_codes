from heapq import heapify, heappushpop
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        wq = [(w/q, q) for w, q in zip(wage, quality)]
        wq.sort()
        q = [-x[1] for x in wq[:K]]
        sumq = -sum(q)
        heapify(q)
        minp = sumq * (wq[K-1][0])
        for i in range(K, len(wq)):
            sumq += wq[i][1]
            sumq += heappushpop(q,  -wq[i][1])
            minp  = min(minp, sumq * wq[i][0])
        return minp













sol = Solution()
print(sol.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))
