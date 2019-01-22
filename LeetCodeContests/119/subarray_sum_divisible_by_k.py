
class Solution:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        mods = [0] * K
        sums, res = 0, 0
        for i in range(len(A)):
            sums = (((sums + A[i]) % K) + K) % K
            res += mods[sums]
            mods[sums] += 1
        res += mods[0]
        return res

print(Solution().subarraysDivByK([4,5,0,-2,-3,1],5))

class Solution1:
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        m = {0: 1}
        sums, ans = 0, 0
        for num in A:
            sums += num
            sum_p = sums%K
            cnt = m[sum_p] if sum_p in m else 0
            ans += cnt
            m[sum_p] = cnt + 1
        return ans
print(Solution1().subarraysDivByK([4,5,0,-2,-3,1],5))