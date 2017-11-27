import math
class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) < 1 : return []
        index  = 0
        min_diff = abs(arr[index] -x)
        for i in range(1,len(arr)):
            curr = abs(arr[i] -x)
            if curr < min_diff:
                index = i
                min_diff = curr 
        res = []
        left = index - 1
        rite = index + 1
        res.append(arr[index])
        k-=1
        while k > 0:
            if left <0:
                rite += 1
                res.append(arr[rite])
                k -= 1
                continue
            if rite >= len(arr):
                left -= 1
                res.append(arr[left])
                k -= 1
                continue
                
            if abs(arr[left] - x) <= abs(arr[rite] - x):
                left -= 1
                res.append(arr[left])
            else:
                rite += 1
                res.append(arr[rite])
            k -= 1
        return sorted(res)  
        
sol = Solution()
print(sol.findClosestElements([1,2,3,4,5], 4, 3))
	        
        
