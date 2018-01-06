noe = int(input())
arr = [int(x) for x in input().split()]
dicts = {}
for i in arr:
    if i in dicts:
        cnt += 1