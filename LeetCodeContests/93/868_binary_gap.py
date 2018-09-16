'''
868. Binary Gap
User Accepted: 2029
User Tried: 2123
Total Accepted: 2075
Total Submissions: 3180
Difficulty: Easy
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary
representation of N.

If there aren't two consecutive 1's, return 0.

Example 1:

Input: 22
Output: 2
Explanation:
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
Example 2:

Input: 5
Output: 2
Explanation:
5 in binary is 0b101.
Example 3:

Input: 6
Output: 1
Explanation:
6 in binary is 0b110.
Example 4:

Input: 8
Output: 0
Explanation:
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
Note:

1 <= N <= 10^9
'''
#solution by YangZhenjian
class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        pre = -1
        ans = 0
        for i in range(32):
            if N == 0: break
            if (N & 1) == 1:
                if pre >= 0:
                    ans = max(ans, i - pre)
                pre = i
            N >>= 1
        return ans

#my solution

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bn = bin(N)[2:]
        maxs = 0
        lastOne = -1
        for i in range(len(bn)):
            if bn[i] == "1":
                if lastOne == -1: lastOne = i
                else:
                    maxs = max(maxs, i - lastOne )
                    lastOne = i
        return maxs

#solution by awice
class Solution(object):
    def binaryGap(self, N):
        A = [i for i in xrange(32) if (N >> i) & 1]
        if len(A) < 2: return 0
        return max(A[i+1] - A[i] for i in xrange(len(A) - 1))

