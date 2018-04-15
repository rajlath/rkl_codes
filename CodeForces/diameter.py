'''
inputCopy
3 1
2 1 4
output
1
inputCopy
3 0
7 7 7
output
0
inputCopy
6 3
1 3 4 6 9 10
output
3
'''
noe, maxs = [int(x) for x in input().split()]
arr1 = [int(x) for x in input().split()]
arr = sorted(arr1)
mins = int(10e9)
for i in range(noe):
    for j in range(i, noe):
        if arr[j]-arr[i] <= maxs:
            if noe - j + i - 1 < mins:
                mins = noe - j + i - 1
print(mins)

