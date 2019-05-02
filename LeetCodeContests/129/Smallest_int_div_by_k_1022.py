class Solution:
    def smallestRepunitDivByK(self, K):
        poss = [False] * K
        x = 1 % K
        cnt = 1
        while True:
            if x == 0:return cnt
            if poss[x]: return -1
            poss[x] = True
            x = (x * 10 + 1 ) % K
            cnt += 1

class Solution1:
    def smallestRepunitDivByK(self, K):
        curr = 0
        for i in range(1, 9 * K):
            curr = (curr * 10 + 1) % K
            if curr == 0:return i
        return -1


print(Solution1().smallestRepunitDivByK(7))