
'''
Input
5
2 3 1 5 1

Output
3
'''
noe = int(input())
arr = [int(x) for x in input().split()]
mins = arr[-1]
cnt  = 0
for i in range(noe-2, -1, -1):
    if arr[i] > mins:
        cnt += (cnt + 1)
    else:mins = min(mins, arr[i])
print(cnt)

