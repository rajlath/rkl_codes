'''
Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
'''
from itertools import groupby
class Solution(object):
    def largeGroupPositions(self, S):
        from itertools import groupby
        i = 0
        res = []
        for _, g in groupby(S):
            l = len(list(g))
            if l >= 3:
                res.append((i, i + l-1))
            i += l
        return res

'''
solution by crazymerlin
sol = Solution()
print(sol.largeGroupPositions("abbxxxxzzy"))
'''

