'''
Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column
to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not len(matrix) or not len(matrix[0]):return matrix
        rows = [False] * len(matrix)
        cols = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
        return matrix

sol = Solution()
ins = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(sol.setZeroes(ins))


