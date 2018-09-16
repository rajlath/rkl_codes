nots = int(input())
for _ in range(nots):
    lens = int(input())
    arr  = [x for x in input().split()]
    cst  = [int(x) for x in input().split()]
    findx = -1
    if "F" in arr:
        findx = arr.index("F")
        sumsA = sum(cst[0:findx:2])
        sumsB = sum(cst[1:findx:2])
    start = 0
    if sumsA > sumsB:
        start = 0
    else:
        start = 1
    sums = arr[start]
    for i in range(1, nots):
        if arr[i+1] == "J":continu


        sums += cost[start]
        if arr[i] == "J":



