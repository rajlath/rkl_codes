
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        a = [x for x in S if x.isalpha()]
        return ''.join([a.pop() if x.isalpha() else x for x in S])

print(Solution().reverseOnlyLetters("Test1ng-Leet=code-Q!"))