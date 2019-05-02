class Solution:
    def canThreePartsEqualSum(self, A):
        prefix = [0]
        for i in A:
            prefix.append(prefix[-1] + i)
        if prefix[-1] % 3 != 0:return False
        each = prefix[-1] // 3
        allOK= [False] * 3
        for x in prefix[1:]:
            if x == each:
                allOK[0] = True
            if allOK[0] and x == each * 2:
                allOK[1] = True
            if allOK[0] and allOK[1] and x == each * 3:
                return True
        return False

from itertools import accumulate
class Solution1:
    def canThreePartsEqualSum(self, A):
        sums = sum(A)
        if sums % 3 != 0:return False
        each = sums // 3
        valid = 0
        cums  = 0
        for i in A:
            cums += i
            if cums == each:
                valid += 1
                cums = 0
        return valid == 3 and cums == 0




print(Solution1().canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))

