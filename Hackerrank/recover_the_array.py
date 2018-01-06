'''
11
5 4 5 4 3 3 2 1 4 1 4
'''

noe = int(input())
arr = [int(x) for x in input().split()]

i = 0
cnt = 0
while len(arr) > 0:
    pos = arr[0]
    arr = arr[pos+1:]
    cnt += 1
print(cnt)