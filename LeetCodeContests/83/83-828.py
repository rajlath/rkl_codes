
class Solution(object):
    def uniqueLetterString(self, S):
        if not S: return 0
        from bisect import bisect_left
        seen = {}
        count = {}
        seen[S[0]] = 0
        res = [1]
        count[S[0]] = 1
        cur = 1
        mod = 10 ** 9 + 7
        for i in range(1, len(S)):
            c = S[i]
            cur += i - seen.get(c, -1) - count.get(c, 0)
            cur %= mod
            count[c] = i - seen.get(c, -1)
            count[c] %= mod
            res.append(cur)
            seen[c] = i

        return sum(res) % mod

'''

solution by crazymerlin
class Solution {
	    public int uniqueLetterString(String S) {
	        char[] s = S.toCharArray();
	        int n = s.length;
	        int mod = 1000000007;
	        long ret = 0;
	        for(int i = 0;i < s.length;i++){
	        	int l = i-1;
	        	for(;l >= 0 && s[l] != s[i];l--);
	        	int r = i+1;
	        	for(;r < n && s[r] != s[i];r++);
	        	ret += (long)(r-i)*(i-l);
	        }
	        return (int)(ret%mod);
	    }
	}

solution by uwi


class Solution(object):
    def uniqueLetterString(self, S):
        arr = [x for x in S]
        n = len(S)
        mod = 1000000007
        ret = 0
        for i in range(n):
            l = i-1
            while l >=0 and S[l] != S[i]:
                l -= 1
            r = i+1
            while r < n and S[r] != S[i]:
                r += 1
            ret += (i-1) * (i - l)
        return ret%mod
'''

sol = Solution()
print(sol.uniqueLetterString("ABC"))


