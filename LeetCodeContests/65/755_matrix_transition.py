'''
756. Pyramid Transition Matrix My SubmissionsBack to Contest
User Accepted: 58
User Tried: 219
Total Accepted: 58
Total Submissions: 534
Difficulty: Medium
We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`. We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
Example 1:
Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
Note:
bottom will be a string with length in range [2, 100].
allowed will have length in range [0, 350].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.
'''

# CODED BY Tricia Deng https://leetcode.com/totricia/ in python 2


from collections import defaultdict
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        n = len(bottom)
        last = [set(x) for x in bottom]
        rules = defaultdict(set)
        for a,b,c in allowed:
            rules[(a,b)].add(c)
        for ii in range(n-1, 0, -1):
            cur = [None for _ in range(ii)]
            for j in range(ii):
                lef = last[j]
                rig = last[j+1]
                tgt = set()
                for x in lef:
                    for y in rig:
                        res = rules.get((x,y), None)
                        if res is not None:
                            tgt = tgt | res
                if len(tgt) == 0:
                    return False
                cur[j] = tgt
            last = cur
        return True
sol = Solution()
print(sol.pyramidTransition(bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]))
