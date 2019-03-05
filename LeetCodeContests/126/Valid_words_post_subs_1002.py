class Solution:
    def isValid(self, S: str) -> bool:
        while S:
            has = len(S)
            S = S.replace("abc", "")
            if has == len(S):
                break
        return S == ""
