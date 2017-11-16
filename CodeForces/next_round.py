input
'''
8 5
10 9 8 7 7 7 5 5
output
6
input
4 2
0 0 0 0
output
0(
'''
n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
ans  = sum([1 for x in arr  if x >= arr[k] and x > 0])
print(ans)