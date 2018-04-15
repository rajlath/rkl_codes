'''
class Solution {
	    public boolean xorGame(int[] nums) {
	    	int x = 0;
	    	for(int v : nums)x ^= v;
	    	return x == 0 || nums.length % 2 == 0;
	    }
	}
'''

class Solution:
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = 0
        for i in nums:x^=i
        return x==0 or len(nums)%2==0

sol=Solution()
print(sol.xorGame([1, 2, 3]))



