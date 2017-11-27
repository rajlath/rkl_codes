'''
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def isInsideGrid(image,i,j):
            col = len(image[0])
            row = len(image)
            return i >= 0 and i < col and  j >= 0 and j < row



        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        scolor = image[0][0]
        for i in range(4):
            x = sr + dx[i]
            y = sc + dy[i]
            if isInsideGrid(image, x, y) and image[x][y]==scolor:
                        image[x][y] = newColor
        return image


sol = Solution()
print(sol.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == newColor:
            return image
        rn, cn = len(image), len(image[0])
        oldColor = image[sr][sc]

        def dfs(x,y):
            if 0 <= x < rn and 0 <= y < cn and image[x][y] == oldColor:
                image[x][y] = newColor
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y+1)
                dfs(x,y-1)
        dfs(sr,sc)
        return image