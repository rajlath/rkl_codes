from collections import Counter
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A:  List[int]
        :rtype:   int
        """
        AC = Counter(A)
        le = len(A)//2
        for i, v in AC.items():
            if v == le:
                return i

print(Solution().repeatedNTimes([5,1,5,2,5,3,5,4]))
