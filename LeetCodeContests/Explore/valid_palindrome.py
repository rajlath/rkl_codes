from string import ascii_lowercase, digits
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valids = ascii_lowercase + digits
        s = [x.lower() for x in s if x.lower() in valids]
        return s == s[::-1]


sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))