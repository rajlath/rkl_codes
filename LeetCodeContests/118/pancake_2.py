class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        n   = len(A)
        ans = []
        for i in range(n, 1, -1):
            t = A.index(i)
            if t != i - 1:
                if t != 0:
                    ans.append(t+1)
                    A = A[:t+1][::-1] + A[t+1:]
                ans.append(i)
                A = A[:i][::-1] + A[i:]
        return ans

print(Solution().pancakeSort([3,2,4,1]))