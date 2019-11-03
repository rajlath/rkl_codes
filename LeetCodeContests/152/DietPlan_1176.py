from itertools import accumulate
class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        lens = len(calories)
        '''
        sums = [0] * (lens + 1)
        for i in range(lens):
            sums[i + 1] = sums[i] + calories[i]
        '''
        sums = [0] + list(accumulate(calories))
        print(sums)
        points = 0
        i = 0
        while (i + k) <= lens:
            current = sums[i + k] - sums[i]
            points += current > upper
            points -= current < lower
            i += 1
        return points

print(Solution().dietPlanPerformance([3,2], 2, 0, 1))