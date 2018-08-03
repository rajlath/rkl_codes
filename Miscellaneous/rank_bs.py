def rank_bs(key, arr):
    '''
    binary search for a value in a sorted array
    param key : value to search type: int | Double
    param arr : arr to search   type: sorted array of int | double
    param lo  : lowest index of arr
    param hi  : highest index of arr
    return    : -1 if not found else index of the value in arr
    '''
    lo  = 0
    hi  = len(arr) - 1
    while lo < hi   :
        mid = lo + (hi - lo) //2
        if   key < arr[mid]:hi = mid - 1
        elif key > arr[mid]:lo = mid + 1
        else:               return mid
    return -1

print(rank_bs(34, [1, 4, 6, 8, 12, 34, 78]))

