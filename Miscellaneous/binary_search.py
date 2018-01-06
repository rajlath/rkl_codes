import random

def create_random_arr(low, high, step, size):
    lst = []
    for i in range(size):
        lst.append(random.randrange(low, high, step))
    return lst

def binary_search(arr, to_find):
    size = len(arr)
    arr  = sorted(arr)
    low  = 0
    high = size -1


    while low <= high:
        mid  = low + (high - low) // 2
        if arr[mid] == to_find:return True
        else:
            if arr[low] < to_find:
                low = mid + 1
            else:
                high= mid - 1
    return False

arr = create_random_arr(10, 1000, 1, 50)
srch= random.randint(10, 1000)
srch1= random.choice(arr)
print(arr, srch)
print(arr, srch1)
print(binary_search(arr, srch))
print(binary_search(arr, srch1))




