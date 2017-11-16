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
from itertools import combinations
word, plen = input().split()
plen = int(plen)
for i in range(1, plen+1):
    lst = (combinations(sorted(word), i))
    for a in lst:
        print("".join(a))

