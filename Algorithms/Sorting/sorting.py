'''
implementation of some types of sorting algorithm
'''
#helpers
def less(a, b):
    '''
    return True if a > b else False
    '''
    return a < b
def swap(arr, a, b)    :
    '''
    a, b are the index to be swapped.
    '''
    arr[a],arr[b] = arr[b],arr[a]
    return arr

def is_sorted(arr):
    '''
    check if array is already sorted.
    return Boolean: True if sorted else False
    '''
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:return False
    return True

def selection_sort(arr):
    '''
    sort arr using selection sort algo.
    '''
    lens = len(arr)
    for i in range(lens):
        mins = i
        for j in range(i+1, lens):
            if less(arr[j] , arr[mins]):mins = j
        arr = swap(arr, i, mins)
    return arr

def insertion_sort(arr)    :
    '''
    sort arr using insertion sort algo.
    '''
    lens = len(arr)
    for i in range(lens):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1],arr[j]
            j -= 1
    return arr

def shell_sort(arr):
    lens = len(arr)
    gaps = lens // 2
    while gaps > 0:
        for i in range(gaps, lens):
            val = arr[i]
            j = i
            while j >= gaps and arr[j - gaps] > val:
                arr[j] = arr[j - gaps]
                j -= gaps
            arr[j] = val
        gaps //= 2
    return arr

def merge_sort(arr)    :
    if len(arr) < 2:
        return arr
    else:
      return list(merge(merge_sort(arr[:len(arr)//2]) ,  merge_sort(arr[len(arr)//2:])))

def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)










import random
import time
from heapq import merge
arrs = random.sample(range(1, 10000), 20)
s = time.clock()
a =insertion_sort(arrs)
print((time.clock() - s) * 10000)
s = time.clock()
a = selection_sort(arrs)
print((time.clock() - s) * 10000)
s = time.clock()
a = shell_sort(arrs)
print((time.clock() - s) * 10000)
s = time.clock()
a = merge_sort(arrs)
print((time.clock() - s) * 10000)



