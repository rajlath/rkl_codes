class Solution:
def largestPerimeter(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    A = sorted(A, reverse=True)
    find = 0
    for i in range(len(A) - 2):
        candidate = A[i:i+3]
        if candidate[0] < candidate[1] + candidate[2]:
            return sum(candidate)
    return 0

class Solution1:
        def largestPerimeter(self, A):
                """
                :type A: List[int]
                :rtype: int
                """
                A = sorted(A)
                for i in range(len(A) - 1, 1, -1):
                if A[i - 2] + A[i - 1] > A[i]:
                        return A[i - 2] + A[i - 1] + A[i]
                return 0