'''
Examples
inputCopy
4 2 1
2 2 1 2 3 2 2 3
outputCopy
7
inputCopy
2 1 0
10 10
outputCopy
20
inputCopy
1 2 1
5 2
'''
n, k, l = [int(x) for x in input().split()]
staves  = [int(x) for x in input().split()]
staves = sorted(staves)
volume = 0
curr   = 0
for i in range(n*k-1, -1, -1):
    curr += 1
    if staves[i] - staves[0] <= l and curr >= k:
        volume += staves[i]
        curr -= k
print([volume, 0][curr > 0])