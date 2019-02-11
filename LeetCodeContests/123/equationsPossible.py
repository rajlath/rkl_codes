class Solution(object):
def equationsPossible(self, equations):
    """
    :type equations: List[str]
    :rtype: bool
    """
    uf = {}
    def find(x):
        if x not in uf: uf[x] = x
        s = []
        while uf[x] != x:
            s.append(x)
            x = uf[x]
        for y in s: uf[y] = x
        return x
    for eq in equations:
        if '==' not in eq: continue
        a, b = find(eq[0]), find(eq[-1])
        # should compare rank but whatever
        uf[a] = b
    for eq in equations:
        if '!=' not in eq: continue
        a, b = find(eq[0]), find(eq[-1])
        if a == b: return False
    return True