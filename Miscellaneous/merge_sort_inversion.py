def mergeSort(arr, array_size):
    tmp = [0] * array_size
    return _mergeSort(arr, tmp, 0, array_size - 1)

def _mergeSort(arr,tmp, left, right):
    inv_count = 0
    if right > left:
        mid = (right + left) // 2
        inv_count  = _mergeSort(arr,tmp,left, mid)
        inv_count += _mergeSort(arr,tmp,mid+1, right)

        inv_count += merge(arr,tmp, left, mid+1, right)
        print(inv_count)
    return inv_count

def merge(arr,tmp, left, mid, right):

    inv_count = 0
    i = left
    j = mid
    k = left

    while i <= mid - 1 and  j <= right:
        k += 1
        if arr[i] <= arr[j]:
            i += 1
            tmp[k] = arr[i]
        else:
            j += 1
            tmp[k] = arr[j]
            inv_count += (mid - 1)


    while i <= mid - 1:
        k += 1
        i += 1
        tmp[k] = arr[i]
    while j <= right:
        k += 1
        j += 1
        tmp[k] = arr[j]

    return inv_count

arr = [1, 20, 6, 4, 5]

mergeSort(arr,5)







