class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:return []
        valids = []
        candidates.sort()
        def backtracks(begin,curr_sum, arr):
            if begin >= len(candidates):return
            for i in range(begin, len(candidates)):
                if candidates[i] + curr_sum == target:
                    valids.append(arr + [candidates[i]])
                    return
                elif candidates[i] + curr_sum > target:return
                else:
                    backtracks(i, curr_sum + candidates[i], arr + [candidates[i]])
        backtracks(0, 0, [])
        return valids
print(Solution().combinationSum([2,3,5], 8))
