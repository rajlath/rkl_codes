def subarr_product(arr, val):
    n = len(arr)
    start = 0
    ends  = 0
    p = 1
    res = 0
    while ends < n:
        p *= arr[ends]
        if p > val:
            while start <= ends and p > val:
                p /= arr[start]
                start += 1
        if p == val:
            countOnes = 0
            while ends + 1 < n and arr[ends + 1] == 1:
                countOnes += 1
                ends += 1
            res += (countOnes + 1    )
            while start <= ends and arr[start] == 1:
                res += (countOnes + 1)
                start += 1
            p //= arr[start]
            start+=1
        ends += 1
    return res



for _ in range(int(input())):
    noe, vals = [int(x) for x in input().split()]
    arr       = [int(x) for x in input().split()]
    print(subarr_product(arr, vals))
