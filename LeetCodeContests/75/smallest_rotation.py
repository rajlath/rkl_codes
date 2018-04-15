'''
Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
"gcmbf"
"fgcmb"
'''
class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool

        def rotate(input,d):
            Lfirst = input[0 : d]
            Lsecond = input[d :]
            Rfirst = input[0 : len(input)-d]
            Rsecond = input[len(input)-d : ]
            if  (Lsecond + Lfirst) == B or (Rsecond + Rfirst) == "B":
                return True
        """
        return len(A) == len(B) and B in A+A


sol = Solution()
print(sol.rotateString('abcde', 'abced'))