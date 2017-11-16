import sys
from collections import defaultdict

def tree():
    return defaultdict(tree)



def boss(d, keys):
    return ', '.join(
        '{} [{}]'.format(e, boss(d, sorted(d[e].keys()))) if d[e]
        else '{}'.format(e)
        for e in keys
    )


with open(input(), 'r') as cef:
    for line in cef:
        d, h = defaultdict(tree), None
        for e in line.split('|'):
            a, b = e.strip()
            d[a][b]
            if h is None:
                h = a              
        print(boss(d, [h]))


