'''
718. Maximum Length of Repeated Subarray My SubmissionsBack to Contest

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        l1 = len(A)
        l2 = len(B)
        f = [[0]*l2 for _ in range(l1)]
        for i in range(l1):
            for j in range(l2):
                if A[i] == B[j]:
                    if i>0 and j>0:
                        this = f[i-1][j-1] + 1
                    else:
                        this = 1
                    f[i][j] = max(f[i][j], this)
        return max(map(max, f))


sol = Solution()
print(sol.findLength([1,2,3,2,1], [3,2,1,4,7] ))