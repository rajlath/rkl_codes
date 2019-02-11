from random import shuffle
def partition(arr, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if arr[i] <= arr[begin]:
            pivot_idx += 1
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
        arr[pivot_idx], arr[begin] = arr[begin], arr[pivot_idx]
    return pivot_idx

def quick_sort_rec(arr, begin, end):
    if begin > end: return
    pivot_idx = partition(arr, begin, end)
    quick_sort(arr, begin, pivot_idx-1)
    quick_sort(arr, pivot_idx+1, end)
    return arr

def quick_sort(arr, begin=0, end=None)    :
    if end == None:end = len(arr) - 1
    return quick_sort_rec(arr, begin, end)




arr = list(range(1, 20))
shuffle(arr)
print(arr)
arr = quick_sort(arr)
print(arr)
