#Thanks to badgergo
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ws = text.split()
        return [ws[i + 2] for i in range(len(ws) - 2) if ws[i] == first and ws[i + 1] == second]

#My Solution
#
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        has = [x for x in text.split()]
        ans = []
        for i in range(len(has) - 2):
            if has[i] == first and has[i+1] == second:
                ans.append(has[i+2])
        return ans
