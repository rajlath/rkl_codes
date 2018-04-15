class Solution(object):
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """
        if self.check(K): return 5
        return 0

    def check(self, K):
        left=0
        right=1000000000
        while left<=right:
            mid=left+(right-left)/2
            x=mid
            base=5
            while mid>=base:
                x+=mid/base
                base*=5
            if x==K: return True
            if x<K: left=mid+1
            else: right=mid-1
        return False


sol = Solution()
print(sol.preimageSizeFZF(0))