class Solution:
    def mincostTickets(self, days, costs) -> int:
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        valid_days = [0] * 366
        for i in days:
            valid_days[i] = 1
        all_days = [0] * 366
        for i in range(1, 366):
            if valid_days[i] == 0:
                all_days[i] = all_days[i-1]
            else:
                one = all_days[max(0, i -  1)] + costs[0]
                sev = all_days[max(0, i -  7)] + costs[1]
                mon = all_days[max(0, i - 30)] + costs[2]
                all_days[i] = min(one, sev, mon)
        return all_days[365]


print(Solution().mincostTickets( [1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))

"""
class Solution(object):
def mincostTickets(self, days, costs):

    c = [
        (1, costs[0]),
        (7, costs[1]),
        (30, costs[2])
    ]
    best = [0] * 30
    days = set(days)
    for i in xrange(1, max(days)+1):
        if i not in days:
            best.append(best[-1])
            continue
        best.append(min(best[-dur] + cost for dur, cost in c))
    return best[-1]
"""