for _ in range(int(input())):
    noe, mods = [int(x) for x in input().split()]
    arr       = [int(x)%mods for x in input().split()]
    pre_sum   = [[0, arr[0]]]
    for i in range(1, noe):
        pre_sum.append([i, (pre_sum[i-1][1] + arr[i])%mods])
    maxs = max(arr)

    pre_sum = sorted(pre_sum, key = lambda x: x[1])
    maxs = max(maxs, pre_sum[noe - 1][1])
    for i in range(noe - 1):
        if pre_sum[i][0] > pre_sum[i + 1][0]:
            val = (pre_sum[i][1] - pre_sum[i + 1][1] + mods)
            maxs = max(val, maxs)
    print(maxs)

