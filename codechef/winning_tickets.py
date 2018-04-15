'''
5
129300455
5559948277
012334556
56789
123456879
'''
from collections import defaultdict
all_set = ["1","2","3","4","4","5","6","7","8","9","0"]
needed  = defaultdict(int)
pairs   = 0
for i in range(int(input())):
    ins = list(input())
    ins = sorted(set(ins))
    ins = list(set(all_set) - set(ins))
    if repr(ins) in needed:
        pairs += needed[repr(ins)]
    needed[repr(ins)] += 1
print(needed)
print(pairs)


