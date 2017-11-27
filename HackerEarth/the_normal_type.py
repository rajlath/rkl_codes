'''
Given an array of numbers
Need to find all subarray that contains count of distinct
elements equal to distinct elements in array.

The Normal Type
SAMPLE INPUT
5
1 2 2 1 1
SAMPLE OUTPUT
8

solution : sliding windows
'''
from collections import defaultdict
noe = int(input())
arr = [int(x) for x in input().split()]

distinct_in_arr = len(set(arr))
dedict = defaultdict(int)
right, window, ans = 0, 0, 0
for left in range(noe):
    while right < noe and window < distinct_in_arr:
        curr = arr[right]
        dedict[curr] = dedict.get(curr, 0) + 1
        if dedict[curr] == 1:
            window += 1
        right += 1
    if window == distinct_in_arr:
        ans += noe - right + 1
    leftar = arr[left]
    dedict[leftar]-=1
    if dedict[leftar] == 0:window -= 1
print(ans)




