from collections import Counter
    class Solution:
        def commonChars(self, A: List[str]) -> List[str]:
            ac = Counter(A[0])
            for i in A[1:]:
                bc = Counter(i)
                ac &= bc
            return list(ac.elements())