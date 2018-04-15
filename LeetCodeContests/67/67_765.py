'''
765. Couples Holding Hands My SubmissionsBack to Contest
User Accepted: 215
User Tried: 343
Total Accepted: 220
Total Submissions: 685
Difficulty: Hard
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that
every couple is sitting side by side. A swap consists of choosing any two people,
then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order,
the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-
'''
#my version of solution submitted by Huize Wang  : huizew

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """

        ans = 0
        for i in range(0, len(row), 2):
            x = row[i]
            need =  [x-1, x+1][x % 2 == 0]
            if need == row[i+1]:
                continue
            t = next(i for i in range(len(row)) if row[i] == need)
            row[i+1], row[t] = row[t], row[i+1]
            ans += 1
        return ans

sol = Solution()
print(sol.minSwapsCouples([3, 2, 0, 1]))