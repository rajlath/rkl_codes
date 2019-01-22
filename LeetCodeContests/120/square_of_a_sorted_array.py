class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(x**2 for x in A)
        
print(Solution().sortedSquares([-4,-1,0,3,10]))
