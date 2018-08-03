class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if any(c.isdigit() for c in S):
            l = "".join(c for c in S if c.isdigit())
            if len(l) == 10:
                return "***-***-" + l[-4:]
            else:
                return "+" + "*" * (len(l) - 10) + "-***-***-" + l[-4:]
        else:
            parts = S.lower().split("@")
            parts[0] = parts[0][0] + "*" * 5 + parts[0][-1]
            return "@".join(parts)
#courtsey crazymerlin