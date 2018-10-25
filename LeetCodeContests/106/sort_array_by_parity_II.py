class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = [0]*len(A)
        e = 0
        o = 1
        for i in A:
            if i % 2 == 0:
                res[e]= i
                e += 2
            else:
                res[o] = i
                o += 2
        return res

print(Solution().sortArrayByParityII([4,2,5,7]))
