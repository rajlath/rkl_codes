class Solution:
def lastSubstring(self, s: str) -> str:
    maxs = ''
    answ = []
    for i in range(len(s)):
        if s[i:] > maxs:
            maxs = s[i:]
            answ.append(maxs)
    return answ[-1]