'''
740. Delete and Earn My SubmissionsBack to Contest

Difficulty: Medium
Given an array nums of integers, you can perform operations on the array.
In each operation, you pick any nums[i] and delete it to earn nums[i] points.
After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:
Input: nums = [3, 4, 2]
Output: 6
Explanation:
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
Example 2:
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation:
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
Note:

The length of nums is at most 20000.
Each element nums[i] is an integer in the range [1, 10000].


'''
class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = [0] * 10001
        # counts[i] stores the count of i
        for num in nums: counts[num] += 1
        # dp[i] stores the maximum sum towards now you can get by picking i
        max_with_me = [0] * 10001
        max_until_me = [0] * 10001
        for i in range(10001):
            max_with_me[i] = i * counts[i]
            if i >= 2:
                max_with_me[i] += max_until_me[i - 2]
            max_until_me[i] = max_with_me[i]
            if i >= 1:
                max_until_me[i] = max(max_until_me[i], max_until_me[i - 1])

        return max_until_me[10000]

sol = Solution()
print(sol.deleteAndEarn([2, 2, 3, 3, 3, 4]))