'''

'''
from bisect import bisect_left
noe = int(input())
arr = [int(x) for x in input().split()]

s = set([])
arr= sorted(arr)

for elem in arr:
    tmp = str(elem)
    for _ in range(len(tmp)-1):
        tmp = tmp[-1]+tmp[:-1]

        try:
            if tmp[0] != "0" and arr[bisect_left(arr, int(tmp))]==int(tmp) and int(tmp) != elem:
                s.add((min(elem, int(tmp)), max(elem, int(tmp))))
        except:
            pass
print(len(s))





