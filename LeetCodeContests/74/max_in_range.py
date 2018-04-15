class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        start=0
        end=0

        res=0
        while end<len(A):
            while end<len(A) and A[end]<=R: end+=1
            res+=(end-start)*(end-start+1)/2
            count=0
            while start<end:
                if A[start]<L: count+=1
                else: count=0
                res-=count
                start+=1
            while end<len(A) and A[end]>R: end+=1
            start=end
        return res
