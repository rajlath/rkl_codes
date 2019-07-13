from itertools import combinations
import re

def get_numbers(s):
    pats = re.compile(r'(\d+)')
    return [int(x) for x in re.findall(pats, s)]



def ScaleBalanceing(a):
    has, couldbe = a[0], a[1]
    has =get_numbers(has)
    couldbe = get_numbers(couldbe)
    for maybe in couldbe:
        if has[0] + maybe == has[1] or has[0] == has[1] + maybe:
            return str(maybe)
    for pair in combinations(couldbe, 2):
        if ( pair[0] + has[0] == has[1] + pair[1] or
             pair[0] + has[1] == pair[1] + has[0] or
             pair[0] + pair[1] + has[0] == has[1] or
             pair[0] + pair[1] + has[1] == has[0] ):
             return "{},{}".format(min(pair), max(pair))
    return "not possible"

print(ScaleBalanceing(["[13, 4]", "[1, 2, 3, 6, 14]"]))