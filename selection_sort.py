from random import shuffle
def selection_sort(arr):
    for i in range(len(arr)):
        mins = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mins]:
                mins = j
        arr[mins], arr[i] = arr[i], arr[mins]
    return arr

arr = list(range(1, 20))
shuffle(arr)
print(arr)
arr = selection_sort(arr)
print(arr)
