'''
Examples
inputCopy
7 4
3 7 5 1 10 3 20
outputCopy
6
inputCopy
7 2
3 7 5 1 10 3 20
outputCopy
-1
'''
noe, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr = sorted(arr)
if k == 0:
    print(0)
else:
    cand = []
    for i in range(noe-k):
        curr = (arr[i:i+k])
        curr = max(curr)
        cand.append(curr)
        #print(cand)
    if len(set(cand)) == len(cand):
        print(cand[0])
    else:
        print(-1)


