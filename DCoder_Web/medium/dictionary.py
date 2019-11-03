noq = int(input())
dicts = {}
for _ in range(noq):
    k, v = [x for x in input().split()]
    dicts[k] = v
for _ in range(int(input()))    :
    curr = input()
    if curr in dicts:
        print(dicts[curr])
    else:
        print(" ")