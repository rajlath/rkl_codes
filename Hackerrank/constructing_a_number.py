'''
3
1
9
3
40 50 90
2
1 4
'''
for _ in range(int(input())):
    n = int(input())
    arr = [x for x in input().split()]
    s = ''
    for i in range(n):
        s += arr[i]
    sums = sum([int(x) for x in s])
    if sums % 3 == 0:
        print("Yes")
    else:
        print("No")
