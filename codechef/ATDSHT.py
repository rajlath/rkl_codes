'''
Sample Input 1:
2
DEEN
TOM
MONTEDALA
Sample Output 1:
1
Sample Input 2:
1
RAKIB
WOW
Sample Output 2:
-1
'''
from string import ascii_uppercase as lc
nos = int(input())
dicts = dict(zip(lc, [0 for x in range(26)]))
dict1 = dict(zip(lc, [0 for x in range(26)]))
total_char = 0
for i in range(nos):
    s = input()
    total_char += len(s)
    for x in s:
        dicts[x]+=1
alpha = input()
for i in alpha:
    dict1[i] += 1
#print(dicts)
#print(dict1)
needed = 0
for i in lc:
    if dict1[i] < dicts[i]:
        needed += dicts[i] - dict1[i]
if total_char <= len(alpha):
    print(needed)
else:
    print(-1)

