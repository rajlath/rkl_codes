'''
9
10 20 20 10 10 30 50 10 20
'''
pairs = []
nos   = int(input())
arr   = [int(x) for x in input().split()]
cnt = 0
for i in arr:
    if i in pairs:
        cnt += 1
        pairs.remove(i)
    else:
        pairs.append(i)
print(cnt)
