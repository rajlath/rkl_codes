# Thanks to badgergo

class Solution:
    def lastStoneWeightII(self, stones):
        # 1 2 3
        dp = {0}
        for x in stones:
            temp = set()
            for item in dp:
                temp.add(item - x)
                temp.add(item + x)
            dp = temp
            print(dp)
        return min(dp, key=abs)

print(Solution().lastStoneWeightII([2,7,4,1,8,1]))