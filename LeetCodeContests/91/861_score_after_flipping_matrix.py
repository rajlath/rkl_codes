'''
861. Score After Flipping Matrix
User Accepted: 606
User Tried: 691
Total Accepted: 615
Total Submissions: 973
Difficulty: Medium
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.



Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39


Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
'''
class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n,m = len(A),len(A[0])
        for row in A:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]

        ans = n
        for j in range(1, m):
            cnt0 = len([A[i][j] for i in range(n) if A[i][j] == 0])
            ans <<= 1
            ans += max(cnt0, n-cnt0)
        return ans

sol = Solution()
print(sol.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))