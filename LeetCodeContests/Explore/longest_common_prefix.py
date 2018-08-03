'''
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        start = strs[0]
        for i in range(len(start)):
            for str in strs[1:]:
                if i >= len(str) or str[i] != start[i]:
                    return start[:i]
        return start

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
