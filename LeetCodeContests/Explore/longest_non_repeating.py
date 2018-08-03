'''
Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without
repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s)
        if lens == 0: return 0

        last_ch_and_pos = {s[0] : 0}
        longest_till_now= [1] * lens
        for idx in range(1, lens):
            last_pos = last_ch_and_pos.get(s[idx], -1)
            if last_pos < idx - longest_till_now[idx - 1]:
                longest_till_now[idx] = longest_till_now[idx - 1] + 1
            else:
                longest_till_now[idx] = idx - last_pos
            #print(longest_till_now)
            last_ch_and_pos[s[idx]] = idx
        return max(longest_till_now)

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
