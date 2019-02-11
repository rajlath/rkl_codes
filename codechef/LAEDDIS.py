def ceilIndex(A, l, r, key):
    while r - l > 1:
        m = l + (r - l)//2
        if A[m] >= key: r = m
        else: l = m
    return r


def LISL(A, n):
    tails = [0 for i in range(n+1)]
    lens = 0
    tails[0] = A[0]
    lens = 1
    for i in range(1, n):
        if A[i] < tails[0]:
            tails[0] = A[i]
        elif A[i] > tails[lens-1]:
            tails[lens] = A[i]
            lens += 1
        else:
            tails[ceilIndex(tails, -1, lens-1, A[i])] = A[i]
    return lens

nb_test = int(input())
for _ in range(nb_test):
    lens = int(input())
    arr  = [int(x) for x in input().split()]
    print(LISL(arr, lens))



