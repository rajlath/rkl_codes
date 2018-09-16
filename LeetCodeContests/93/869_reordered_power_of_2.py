'''
869. Reordered Power of 2
User Accepted: 1320
User Tried: 1605
Total Accepted: 1337
Total Submissions: 3088
Difficulty: Medium
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that
the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9
'''
#solution by https://leetcode.com/yangzhenjian
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        poss = set()
        for i in range(32):
            poss.add(''.join(sorted(str(1 << i))))

        return ''.join(sorted(str(N))) in poss

#my solution
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        ns = str(N)
        i = 1
        while True:
            if len(str(i)) < len(ns):
                i*=2
                continue
            if sorted(str(i)) == sorted(ns):return True
            if len(str(i)) > len(ns):break
            i *= 2
        return False

#Solution by awice
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        Let's work through an example like N = 128.
        In the last line, 'for cand in itertools.permutations(str(N))' will
        iterate through the six possibilities cand = ('1', '2', '8'),
        cand = ('1', '8', '2'), cand = ('2', '1', '8'), and so on.

        The check cand[0] != '0' is a check that the candidate permutation
        does not have a leading zero.

        The check bin(int("".join(cand))).count('1') == 1 is a check that cand
        represents a power of 2: namely, that the number of ones in its binary
        representation is 1.
        """
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1
                   for cand in itertools.permutations(str(N)))

class Solution(object):
    def reorderedPowerOf2(self, N):
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b))
                   for b in xrange(31))

                   