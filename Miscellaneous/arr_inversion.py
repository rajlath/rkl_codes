'''
implementation of finding inversions in an sorted array
'''
#helper section
def lower_bound(arr, lo, hi, val):
    '''
    finding lower bound of val in the array(sorted) range lo to hi
    type arr : array of integer
    lo       : int start index of the array in which lower bound is searched
    hi       : int end   index of the array in which lower bound in searched
    val      : int value for which lower bound is searched
    rtype    : int lower bound index of the value
    '''
    if val > max(arr):return -1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == val:
            if arr[mid - 1] != val:
                hi = mid
                break
            else:
                hi = mid - 1
        else:
            if arr[mid] > val:
                hi = mid - 1
            else:
                lo = mid + 1
    return -1 if arr[hi] != val else hi

def upper_bound(arr, lo, hi, val):
    '''
    find upper bound of val in the arr range lo to hi
    type arr  : array of integer
    lo        : int start index
    hi        : int end   index
    val       : int value for which upper bound is to be found
    rtype     : int upper bound of val
    '''
    if val > max(arr):return -1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == val:
            if mid + 1 == hi:
                lo = mid
                break
            if arr[mid + 1] != val:
                lo = mid
                break
            else:
                lo = mid + 1
        elif arr[mid] > val:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1 if arr[mid] != val else lo

def get_sum(BIT, indx):
    '''
    get sum in the range 0 to indx of an array
    type BIT : binary tree constructed from array
    type indx: int end index for range sum
    rtype    : int sum of the range
    '''
    sums = 0
    while indx > 0:
        sums += BIT[indx]
        indx -= indx & (-indx)
    return sums

def update_BIT(BIT, n, indx, val):
    '''
    update binary tree BIT when array is updated at indx with val
    type BIT   : binary tree
    type n     : int length of array
    type indx  : int index of BIT to be updated
    type val   : int updated value
    ret  BIT   : updated BIT
    '''
    while indx <= n:
        BIT[indx] += val
        indx += indx & (-indx)
    return BIT

def create_inversion_arr(arr, n):
    '''
    create an array of inversion count for each elements in array
    type arr  : array of int
    type n    : int length of arr
    rtype     : array of integer containing inversion count
    '''
    temp = arr
    temps= sorted(arr)
    iarr = []
    for i in range(n):
        iarr.append(lower_bound(temps, 0, n, arr[i]) + 1)
    return iarr

def get_inversion_count(arr, n):
    arri = create_inversion_arr(arr, n)
    BIT  = [0] * (n + 1)
    inv  = 0
    for i in range(n-1, -1, -1):
        inv += get_sum(BIT, arri[i] - 1)
        update_BIT(BIT, n, arri[i], 1)
    return inv













#arr = [1, 2, 2, 2, 2, 5, 5, 5, 5]
#arr  = [7,-90,100,1]
arr   = [2,3,1,5,4]
print(lower_bound(arr, 0, len(arr), -13))
print(upper_bound(arr, 0, len(arr), 15))
print(create_inversion_arr(arr, len(arr)))
print(get_inversion_count(arr, len(arr)))


