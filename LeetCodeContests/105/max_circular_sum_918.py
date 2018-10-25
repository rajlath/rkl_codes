class Solution:
    def kadane(self, a):
        n = len(a)
        max_so_far = 0
        max_ending_here = 0
        for i in range(n):
            max_ending_here = max_ending_here + a[i]
            if max_ending_here < 0:max_ending_here = 0
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
        return max_so_far

    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        max_kadane = self.kadane(A)

        max_wrap = 0
        for i in range(n):
            max_wrap += A[i]
            A[i] = -A[i]
        max_wrap = max_wrap + self.kadane(A)
        if max_wrap > max_kadane:
            return max_wrap
        else:
            return max_kadane

print(Solution().maxSubarraySumCircular([5,-3,5]))
