'''
Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''
from itertools import permutations
word, plen = input().split()
plen = int(plen)
combs = permutations(word, plen)
combs = sorted(combs)
for a in combs:
    print("".join(a))