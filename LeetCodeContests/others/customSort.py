'''
Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
'''
from string import ascii_lowercase  as lc
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        alphabet = list(S)
        alphabet += [x for x in lc if x not in alphabet]
        alphabet = "".join(alphabet)
        return "".join(sorted(T, key=lambda word: [alphabet.index(c) for c in word]))

sol = Solution()
print(sol.customSortString("cba", "abcd"))