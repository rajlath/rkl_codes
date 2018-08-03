#https://leetcode.com/contest/weekly-contest-86/problems/magic-squares-in-grid/
#oorja.halt@gmail.com
#27th May 2018 10:18
'''
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).
Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
'''

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_it_magic(subgrid):
            '''
            return True if subgrid
            1.all unique integers
            2.sum of rows and cols equals to  15
            sum of numbers from 1 to 9 is 45
            As subgrid has to be all unique elements
            sum of all rows and cols has to be 45/3
            '''
            flatten = [item for sg in subgrid for item in sg]
            if len(set(flatten)) != 9:return False

            if sum(subgrid[0]) == sum(subgrid[1]) == sum(subgrid[2]):
                #print(subgrid[0][0] , subgrid[1][1] , subgrid[2][2] )
                #print(subgrid[0][2] , subgrid[1][1],+ subgrid[2][0] )
                if (subgrid[0][0] + subgrid[1][1] + subgrid[2][2]) == (subgrid[0][2] + subgrid[1][1] + subgrid[2][0] ==15):
                    sub1 = [list(x) for x in zip(*subgrid)]
                    if sum(sub1[0])==sum(sub1[1]) == sum(sub1[2]):
                        return True
            else: return False

        row = len(grid)
        col = len(grid[0])
        cnt = 0
        i = 0
        j = 0
        while i < row - 2:

            while j < col - 2:
                if is_it_magic([grid[i][j:j+3], grid[i+1][j:j+3], grid[i+2][j:j+3]]):cnt += 1
                j += 1
            i+=1
        return cnt

sol = Solution()
ins =[[10,3,5],[1,6,11],[7,9,2]]
print(sol.numMagicSquaresInside(ins))




