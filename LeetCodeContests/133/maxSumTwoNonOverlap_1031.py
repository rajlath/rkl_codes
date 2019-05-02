from itertools import accumulate
class Solution:
    def maxSumTwoNoOverlap(self, A, L, M):
        pre = [0] + A
        lens= len(A)
        pre = list(accumulate(pre))

        def is_valid(i, j):
            return i + L <= lens and j +  M <= lens and (j>=i+L or i>=j+M)

        ans = 0
        for i in range(lens):
            for j in range(lens):
                if is_valid(i, j):
                    ans = max(ans, pre[i+L]-pre[i] + pre[j+M]-pre[j])
        return ans


print(Solution().maxSumTwoNoOverlap([2,1,5,6,0,9,5,0,3,8],4,3))