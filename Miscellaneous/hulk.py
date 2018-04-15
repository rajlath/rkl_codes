'''
Sample Input 0

2
5
10101
0 4
5
10001
3 4
Sample Output 0

0
1
'''
for _ in range(int(input())):
    noe = int(input())
    arr = input()
    l, r = [int(x) for x in input().split()]
    l, r = min(l, r), max(l, r)
    arr = arr[l:r+1]
    last_index = arr.rindex(arr[0])
    if last_index==len(arr)-1:print(0)
    elif 0<last_index<len(arr)-1:print(1)
    else:print(1)
