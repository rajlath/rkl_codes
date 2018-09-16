import random

ages = [random.randint(1, 100) for x in range(20)]

def find_k_largest_quicksort(s, k):
    k_largest = qselect(s, k)
    result = []
    return [x for x in s if x >= k_largest]


def qselect(a, k, left = None, rite = None)    :
    left = left or 0
    rite = rite or len(a)-1
    pivot= random.randint(left, rite)

    pivotV= a[pivot]
    a[pivot], a[rite] = a[rite], a[pivot]
    swapindx = left
    i = left
    while i <= rite - 1:
        if a[i] < pivotV:
            a[i], a[swapindx] = a[swapindx], a[i]
            swapindx += 1
        i += 1
    a[rite], a[swapindx] = a[swapindx], a[rite]
    rank = len(a) - swapindx
    if k == rank:
        return a[swapindx]
    elif k < rank:
        return qselect(a, k, swapindx+1, rite)
    else:
        return qselect(a, k, left, swapindx)


print(ages)
print(sorted(find_k_largest_quicksort(ages, 3)))









