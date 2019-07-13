class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        lens   = len(merged)
        if lens % 2 == 0:
            return (merged[lens//2] + merged[lens//2 - 1])/2
        else:
            return merged[lens//2]

print(Solution().findMedianSortedArrays([1,3],[2]))
