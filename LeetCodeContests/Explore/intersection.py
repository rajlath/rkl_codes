from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = dict()
        ret = []
        for i in nums1:
            map[i] = map.get(i, 0) + 1
        for i in nums2:
            if i in map and map[i] > 0:
                ret.append(i)
                map[i] -= 1
        return ret





sol = Solution()
print(sol.intersect([1,2],[1,1]))