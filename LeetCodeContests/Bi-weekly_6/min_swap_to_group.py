class Solution():
    def minSwaps(self, data):
        lens = len(data)
        ones = data.count(1)
        if ones == 0:return -1
        curr = 0
        for i in range(ones):
            curr += data[i] == 1
        maxs = curr
        for i in range(ones, lens):
            curr += data[i] == 1
            curr -= data[i - ones] == 1
            maxs = max(maxs, curr)
        return ones - maxs


print(Solution().minSwaps([1,0,1,0,1,0,0,1,1,0,1]))          
