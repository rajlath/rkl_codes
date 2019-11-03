class Solution:
    def numPrimeArrangements(self, n):
        p=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        MOD =  1000000007
        pr, nonpr = 0, 0
        for i in range(1, n + 1):
            if i in p:
                pr += 1
            else:
                nonpr += 1
        answer = 1
        for i in range(1, pr + 1):
            answer = (answer * i ) % MOD
        for i in range(1, nonpr + 1):
            answer = (answer * i ) % MOD
        return answer

print(Solution().numPrimeArrangements(100))


