'''
Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest
'''

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        a = points
        xmax = max([x[0] for x in a])
        xmin = min([x[0] for x in a])
        ymax = max([x[1] for x in a])
        ymin = min([x[1] for x in a])

        ans  = ((xmax-xmin)*(ymax-ymin))
        ans  = ans/2
        return ans

sol = Solution()
a = [[1,0],[0,0],[0,1]]
print(sol.largestTriangleArea(a))