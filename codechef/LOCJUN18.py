from collections import deque
n = int(input())
count = 0
arr = [int(x) for x in input().split()]
maxs= max(arr)
brr = []
for i in range(n):
    brr.append(maxs - arr[i] + 1)
    arr[i] += maxs
q = deque()
for i in range(n):
    while q and brr[i] > q[-1]:
        q.pop()
    while q and arr[i] < q[0]:
        q.popleft()
    if arr[i] != brr[i] and (not (q) or brr[i] != q[-1]):
        count += 1
        q.append(brr[i])
print(count)

