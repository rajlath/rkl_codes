from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        n, req = len(s), len(s) // 4
        c_all = Counter(s)
        c_cur = Counter()
        l = -1
        ans = n
        for r in range(n):
            c_cur[s[r]] += 1
            while l < r:
                c_cur[s[l + 1]] -= 1
                flag = all(c_all[ch] - c_cur[ch] <= req for ch in "QWER")
                if flag:
                    l += 1
                else:
                    c_cur[s[l + 1]] += 1
                    break
                if all(c_all[ch] - c_cur[ch] <= req for ch in "QWER"):
                    ans = min(ans, r - l)
                return ans

print(Solution().balancedString("QQWE"))