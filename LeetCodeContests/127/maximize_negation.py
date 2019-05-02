class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        heapq.heapify(A)
        for i in range(K):
            p = heapq.heappop(A)
            if p == 0:
                break
            heapq.heappush(A, -p)
        return sum(A)