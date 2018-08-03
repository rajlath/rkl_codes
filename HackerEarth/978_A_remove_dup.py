'''
6
1 5 5 1 6 1
outputCopy
3
5 6 1
inputCopy
5
2 4 2 4 4
outputCopy
2
2 4
inputCopy
5
6 6 6 6 6
outputCopy
1
6
'''
noe = int(input())
arr = [int(x) for x in input().split()]
seen = []
for i in range(noe-1, -1, -1):
    if arr[i] not in seen:
        seen.append(arr[i])
print(len(seen))
print(*seen[::-1])
