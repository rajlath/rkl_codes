from itertools import groupby
nb_elements = int(input())
elements = [int(x) for x in input().split()]
maxs = max(elements)
ele_Group = groupby(elements)
max_len = 0
for k, g in ele_Group:
    if k == maxs:
        max_len = max(max_len, len(list(g)))
print(max_len)        

