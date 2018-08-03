'''
852. Peak Index in a Mountain Array
User Accepted: 1861
User Tried: 1888
Total Accepted: 1911
Total Submissions: 2465
Difficulty: Easy
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 1:return A[0]
        if len(A) == 2:return max(A[0], A[1])
        low = 0
        high = len(A) - 1
        while low < high:
            mid = (low + high) // 2
            # Compare mid's neighbors
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                # Found max
                return mid
            elif A[mid -1] < A[mid]:
                low = mid
            else:
                high = mid
'''
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(1, len(A)):
            if A[i]>A[i-1] and A[i]>A[i+1]:
                return i
        return -1


sol = Solution()
print(sol.peakIndexInMountainArray([0,2,1,0]))
