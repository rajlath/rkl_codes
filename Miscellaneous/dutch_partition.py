def dutch_partition(arr, indx):
    smaller = 0
    equal   = 0
    larger  = len(arr)-1
    pivot   = arr[indx]
    while equal < larger:
        print("less",arr[equal], pivot )
        if arr[equal] < pivot:
            arr[smaller], arr[equal]= arr[equal], arr[smaller]
            smaller += 1
            equal   += 1
            print(arr)
        elif arr[equal] == pivot:
            print("equal",arr[equal], pivot )
            equal += 1
        else:
            print("more",arr[equal], pivot )
            arr[equal], arr[larger] = arr[larger], arr[equal]
            larger -= 1
    return arr

arr = [-3, 0, -1, 1, 1, 11, 8, 3, 3, 4, 2]
print(dutch_partition(arr, 0))
