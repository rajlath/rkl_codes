def bubble_sort(arr):
    '''
    implementation of bubble sort
    '''
    have_done = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(have_done):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        have_done -= 1
    return arr

def selection_sort(arr)    :
    '''
    implementation of selection sort
    '''
    lens = len(arr)
    for i in range(lens):
        min_index = i
        for j in range(i+1, lens):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

def insertion_sort(arr)    :
    for i in range(1, len(arr)):
        curr_idx = i
        curr_val = arr[i]
        while curr_idx > 0 and arr[curr_idx-1] > curr_val:
            arr[curr_idx] = arr[curr_idx - 1]
            curr_idx -= 1
        arr[curr_idx] = curr_val
    return arr

def quicksort(x):
      if len(x) < 2:
          return x
      else:
          pivot = x[0]
          less = [i for i in x[1:] if i <= pivot]
          greater = [i for i in x[1:] if i > pivot]
          return quicksort(less) + [pivot] + quicksort(greater)












arrs = [54,26,93,17,77,31,44,55,20]
print(bubble_sort(arrs))
print(selection_sort(arrs))
print(insertion_sort(arrs))
print(quicksort(arrs))





