class Solution():
    def canMakePaliQueries(self, s,queries):
        dicts = [{}]
        currs = {}
        for c in s:
            currs[c] = currs.get(c, 0) + 1
            dicts.append({k:v for k, v in currs.items()})
        rets = []
        for left, right, k in queries:
            diff = 0
            for c, n in dicts[right + 1].items():
                if (n - dicts[left].get(c, 0)) % 2:
                    diff += 1
            rets.append(diff >> 1 <= k)
        return rets