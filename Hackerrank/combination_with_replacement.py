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

from itertools import combinations_with_replacement
word, plen = input().split()
plen = int(plen)
lst = (combinations_with_replacement(sorted(word), plen))
for a in lst:
    print("".join(a))
