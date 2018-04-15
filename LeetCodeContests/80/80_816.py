class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:-1]
        def enume_item(item):
            if len(item) == 1: return [item]
            if all(x=='0' for x in item):
                return []
            if item[0] == '0':
                if item[-1] == '0':
                    return []
                return ['0.' + item[1:]]
            if item[-1] == '0':
                return [item]
            return [item[:x] + '.' + item[x:] for x in range(1, len(item))] + [item]
        ans = []
        for sp in range(1, len(S)):
            A, B = S[:sp], S[sp:]
            AC = enume_item(A)
            if not AC: continue
            BC = enume_item(B)
            if not BC: continue
            ans.extend('({0}, {1})'.format(x,y) for x in AC for y in BC)
        return ans