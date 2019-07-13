import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if len(nums) == 0:
            return []
        if k == 1 or len(nums) == 1:
            return map(lambda x: float(x), nums)
        # general
        # function
        def BS(l,n):
            """
            :type l: List[int]
            :type n: int
            :rtype int
            """
            lo = 0
            hi = len(l)-1
            mi = 0
            while lo < hi-1:
                mi = lo + (hi-lo)//2
                if l[mi] == n:
                    return mi
                elif l[mi] < n:
                    lo = mi
                else:
                    hi = mi
            if l[mi] < n:
                while mi<len(l) and l[mi] < n:
                    mi += 1
                return mi
            else:
                while mi>=0 and l[mi] > n:
                    mi -= 1
                return mi + 1

        if k%2 == 1:
            # sort
            ori = sorted(nums[:k])
            result = [float(ori[len(ori)//2])]
            # loop
            for i in range(k,len(nums)):
                ori.remove(nums[i-k])
                new = ori
                new.insert(BS(new,nums[i]),nums[i])
                result.append(float(new[len(new)//2]))
                ori = new
        else:
            # sort
            ori = sorted(nums[:k])
            result = [float((ori[len(ori)//2-1]+ori[len(ori)//2])/2.)]
            # loop
            for i in range(k,len(nums)):
                ori.remove(nums[i-k])
                new = ori
                new.insert(BS(new,nums[i]),nums[i])
                result.append(float((new[len(new)//2-1]+new[len(new)//2])//2.))
                ori = new

        return result

lens, ksize = [int(x) for x in input().split()]
elements    = [int(x) for x in input().split()]
answer = Solution().medianSlidingWindow(elements, ksize)
print(*list(map(int, answer)))

#10 2
#4 4 3 2 10 1 2 7 10 2
#4 3 2 2 1 1 2 7 2