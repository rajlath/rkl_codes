def remove_duplicate_in_array(arr):
    '''
    given an array of  whole numbers with remove
    all elements that are repeated.
    type  : array of integers
    rtype : array of integers having distinct values only
    '''

    uniques = []
    for i in arr:
        if i not in uniques:
            uniques.append(i)
    return uniques

def remove_duplicate_in_array_1(arr):
    '''
    sort arr and iterate and skip duplicate elements.
    '''
    arr = sorted(arr)
    previous = arr[0]
    rets = [arr[0]]
    for i in arr[1:]:
        if i == previous:
            continue
        else:
            rets.append(i)
            previous = i
    return rets



import random
arr  = [random.randrange(1000) for _ in range(10)]
arr.append(arr[5])
arr.append(arr[8])

arrs = remove_duplicate_in_array(arr)
print(arr, arrs, len(arr), len(arrs))
#[814, 901, 25, 991, 312, 924, 72, 856, 71, 787, 924, 71]
#[814, 901, 25, 991, 312, 924, 72, 856, 71, 787]
#12 10


arrs = remove_duplicate_in_array_1(arr)
print(arr, arrs, len(arr), len(arrs))
#[814, 901, 25, 991, 312, 924, 72, 856, 71, 787, 924, 71]
#[814, 901, 25, 991, 312, 924, 72, 856, 71, 787]
#12 10




