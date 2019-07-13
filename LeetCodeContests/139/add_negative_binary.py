class Solution():
    def addNegabinary(self, arr1, arr2):
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        sum1 = sum([(-2) ** i if arr1[i] == 1 else 0 for i in range(len(arr1))])
        sum2 = sum([(-2) ** i if arr2[i] == 1 else 0 for i in range(len(arr2))])

        sums = sum1 + sum2

        def base_neg_2(N):
            if N == 0 or N == 1: return str(N)
            return base_neg_2(-(N >> 1)) + str(N & 1)

        s = base_neg_2(sums)
        #print(s)
        ans = [int(s[i]) for i in range(len(s))]
        return ans

print(Solution().addNegabinary([1,1,1,1,1], [1,0,1]))
