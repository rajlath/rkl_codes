'''
Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
'''
class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type dominoes: str
        :rtype: str
        """
        if rec1[2] <= rec2[0] or rec1[3] <= rec2[1]:
            return False
        if rec1[0] >= rec2[2] or rec1[1] >= rec2[3]:
            return False
        return True

sol = Solution()
print(sol.isRectangleOverlap([0,0,2,2],[1,1,3,3]))






