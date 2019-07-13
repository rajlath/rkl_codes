class Solution:
    def maxArea(self, height: List[int]) -> int:
        def calculateArea(i, j):
            return (j-i)*(min(height[i], height[j]))
        i, j, area = 0, len(height)-1, 0
        while(i < j):
            if(height[i]>height[j]):
                area = max(area, calculateArea(i, j))
                j -= 1
            else:
                area = max(area, calculateArea(i, j))
                i += 1
        return (area)
