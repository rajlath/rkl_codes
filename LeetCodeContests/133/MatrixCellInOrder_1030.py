class Solution:
    def twoCitySchedCost(self, costs):
        base = 0
        lens = len(costs)
        cs = [0] * lens
        p  = 0
        for c in costs:
            base += c[0]
            cs[p] = c[1] - c[0]
            p += 1
        cs.sort();
        return base + sum(cs[:lens//2])

print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))