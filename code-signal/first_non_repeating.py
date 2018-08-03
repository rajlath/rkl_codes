from collections import OrderedDict
def firstNotRepeatingCharacter(s):
    sc = OrderedDict()
    ans = ""
    for i in s:
        sc[i] = sc.get(i, 0)+1
    for i, v in sc.items():
        if v == 1:
            return i
    return "_"




print(firstNotRepeatingCharacter("abacabad"))