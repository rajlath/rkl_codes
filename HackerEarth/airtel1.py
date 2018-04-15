'''
4
1 2 1 2
'''
soa = int(input())
arr = [-1 if int(x)&1 else 1 for x in input().split()]
hashmap = {}
sums = 0
cnt  = 0
for i, x in enumerate(arr):
    hashmap[i] = arr[i]
    sums += [1, -1][arr[i]%2]
    if sums == 0:cnt += 1
print(cnt)