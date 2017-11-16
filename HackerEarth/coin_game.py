import sys
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    cnt = 0
    for i in arr:
        s = i
        while not s & 1:
            cnt += 1
            s //= 2
    print(["Alan", "Charlie"][cnt % 2])            
