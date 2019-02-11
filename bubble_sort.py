from random import shuffle
def bubble_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x += 1
        for i in range(1, n-x):
            if arr[i-1] > arr[i]:
                swap(i-1, i)
                swapped = True
        print(arr)
    return arr

arr = list(range(1, 10))
shuffle(arr)
print(arr)
arr = bubble_sort(arr)
print(arr)
