'''
Aditya Priya Kshitij Priya Anandita Aditya Aditya Priya Kshitij Kshitij
'''
from collections import Counter
noe = int(input())
lst = Counter([x for x in input().split()])
maxs = lst.most_common()[0][1]
grtr = []
for i, v in lst.items():
    if v==maxs:
        grtr.append(i)
print(sorted(grtr,)[-1])

