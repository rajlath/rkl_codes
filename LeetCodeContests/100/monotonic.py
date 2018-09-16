class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return  all(a >= b for a, b in zip(A,A[1:])) or all(a <= b for a, b in zip(A, A[1:]))
