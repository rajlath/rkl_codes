from collections import Counter

class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        result = []

        max_cnt = [0] * 26

        for w in B:
            cnt = Counter(w)
            for key, value in cnt.items():
                idx = ord(key) - ord('a')
                max_cnt[idx] = max(max_cnt[idx], value)

        for w in A:
            cur_cnt = [0] * 26
            for x in w:
                cur_cnt[ord(x) - ord('a')] += 1
            ok = True
            for i in range(26):
                if cur_cnt[i] < max_cnt[i]:
                    ok = False
                    break

            if ok:
                result.append(w)

        return result