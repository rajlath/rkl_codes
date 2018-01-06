
'''
754. Reach a Number My SubmissionsBack to Contest
User Accepted: 304
User Tried: 933
Total Accepted: 316
Total Submissions: 2960
Difficulty: Easy
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].
'''
class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        pos = 0
        inc = 0
        while pos < target or (pos - target) & 1:
            inc += 1
            pos += inc
        return inc

sol = Solution()
print(sol.reachNumber(int(input())))