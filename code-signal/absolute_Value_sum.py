def absoluteValuesSumMinimization(a):
    if not len(a)%2:
        return a[len(a)//2 -1]
    else:
        return a[len(a)//2]

    return A[len(A) // 2 + len(A) % 2 - 1]