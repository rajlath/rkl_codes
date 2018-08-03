from bisect import bisect_right

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        N = len(difficulty)
        M = len(worker)
        jobs = sorted([(difficulty[i], -profit[i]) for i in xrange(N)])
        difs = [0]
        profs = [0]
        for d, p in jobs:
            profit = -p
            if profit > profs[-1]:
                profs.append(profit)
                difs.append(d)
        total = 0
        for w in worker:
            i = bisect_right(difs, w) - 1
            total += profs[i]
        return total



    class Solution(object):
        def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = zip(difficulty, profit)
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans