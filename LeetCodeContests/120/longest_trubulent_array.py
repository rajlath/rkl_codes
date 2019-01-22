class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans=1
        cur=[1,1]
        for i in range(1,len(A)):
            if A[i]==A[i-1]:
                cur=[1,1]
            elif A[i]>A[i-1]:
                cur=[1,cur[0]+1]
            else:
                cur=[cur[1]+1,1]
            ans=max(ans,max(cur))
        return ans
