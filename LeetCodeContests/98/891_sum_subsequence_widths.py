'''
891. Sum of Subsequence Widths

Difficulty: Hard
Given an array of integers A, consider all non-empty subsequences of A.

For any sequence S, let the width of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A.

As the answer may be very large, return the answer modulo 10^9 + 7.



Example 1:

Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.


Note:

1 <= A.length <= 20000
1 <= A[i] <= 20000
'''
class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        A.sort()
        n = len(A)
        pow2 = [1]
        for _ in range(n+1):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, a in enumerate(A):
            ans -= a * (pow2[n-i-1] - 1) % MOD
            ans += a * (pow2[i] - 1) % MOD
            ans = (ans + MOD) % MOD
        return ans
