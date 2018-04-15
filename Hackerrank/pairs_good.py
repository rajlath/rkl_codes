'''
6
10 1 13 31 23 32 12456  45621
'''
from collections import defaultdict
def myhash(s):
    return sum([ord(x) for x in s])

def validate(arr, a, b,pairs):
    #print(arr[a], arr[b])
    if ((arr[a], arr[b]) not in pairs):
        if len(arr[a]) == len(arr[b]):
            if arr[a] != arr[b]:
                if arr[a][0] == arr[b][-1] or arr[a][-1] == arr[b][0]:
                    return True
    return False




from collections import defaultdict
noe = input()
arr = [x for x in input().split()]
recycle = defaultdict(list)
cnt = 0
pairs = []
for i, s1 in enumerate(arr):
    hashe = myhash(s1)
    if hashe in recycle:
        if validate(arr, i, recycle[hashe], pairs):
            pairs.append((s1, arr[recycle[hashe]]))
            #print(pairs)
    else:
        recycle[hashe] = i
print(len(pairs))



