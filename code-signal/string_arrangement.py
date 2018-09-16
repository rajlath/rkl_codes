def check(p):
    for i in range(1, len(p)):
        if count(p[i], p[i-1]) != 1:
            return False
    return True


def count(s1, s2):
    return sum([1 for a, b in zip(s1, s2) if a != b])

import itertools
def stringsRearrangement(inputArray):
    perms = list(itertools.permutations(inputArray))
    ans = False
    for i in perms:
        if check(i): return True
    return False



print(stringsRearrangement(["aba", "bbb", "bab"]))







