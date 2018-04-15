class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        count_dict = defaultdict(int)
        for url in cpdomains:
            counts, uri = url.split()
            counts = int(counts)
            urpars = uri.split(".")
            for i in range(len(urpars)):
                curr = ".".join(urpars[i:])
                count_dict[curr] = count_dict.get(curr, 0) + counts
        rets = []
        for k, v in count_dict.items():
            rets.append(str(v) +" "+k)
        return rets

sol = Solution()
print(sol.subdomainVisits(["9001 discuss.leetcode.com"]))

