MOD =  1000000007
for _ in range(int(input())):
    curr = int(input())
    if curr == 0:print(0, 0)
    else:
        maxs = pow(2, curr-1, MOD)
        print((maxs - 1)%MOD, maxs)

