'''
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.



Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
'''
class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        ans = 0
        for i in range(1, size-1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                l = i - 1
                r = i + 1
                while l > 0 and A[l] > A[l-1]: l-= 1
                while r < size-1 and A[r] > A[r+1]: r +=1
                ans = max(ans, r - l + 1)
        return ans

sol = Solution()
print(sol.longestMountain([0,1,2,3,4,5,4,3,2,1,0]))


