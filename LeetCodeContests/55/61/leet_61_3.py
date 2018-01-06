'''
740. Delete and Earn My SubmissionsBack to Contest
User Accepted: 359
User Tried: 621
Total Accepted: 364
Total Submissions: 1388
Difficulty: Medium
Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

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
Each element nums[i] is an integer in the range [1, 10000]
'''
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = [0]*10003
        total = [0]*10003
        for i in nums:
            total[i] += i
        f[0] = total[0]
        f[1] = total[1] if total[1] > total[0] else total[0]
        for i in range(2, 10001):
            if f[i] < f[i-1]:
                f[i] = f[i-1]
            if f[i] < f[i-2] + total[i]:
                f[i] = f[i-2] + total[i]
        return f[10000]

'''
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int n = 10001;
        vector<int> fre(n, 0);
        for (auto num: nums) {
            fre[num]++;
        }

        vector<int> dp(n, 0);
        dp[1] = fre[1];

        for (int i = 2; i < n; i++) {
            dp[i] = max(dp[i - 1], dp[i - 2] + i * fre[i]);
        }

        return dp[n - 1];
    }
};
'''
from collections import Counter

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ct = Counter(nums)
        vals = sorted(list(ct.iteritems()))
        dpprev = 0
        dplast = vals[0][1] * vals[0][0]
        #print dpprev, dplast
        #print vals
        for i, v in enumerate(vals):
            if i == 0:
                continue
            num, ct = v
            if vals[i-1][0] == num-1:
                aux = dplast
                dplast = dpprev + ct*num
                dpprev = max(aux, dpprev)
            else:
                aux = dplast
                dplast = max(dplast, dpprev) + ct*num
                dpprev = max(aux, dpprev)
            #print dpprev, dplast
        return max(dplast, dpprev)

        