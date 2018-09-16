'''
1
1 1
5
'''
nots = int(input())
for _ in range(nots):
    lens, k = [int(x) for x in input().split()]
    ans  = 0
    arr = [int(x) for x in input().split()]
    for i in arr:
        ans = max(abs(ans), abs(i))
    print("1", ans)


