def sort_even_odd(arr):
    next_even = 0
    next_odd  = len(arr)-1
    while next_even < next_odd:
        if arr[next_even] & 1:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1
        else:
            next_even += 1
    return arr

print(sort_even_odd([12,89,45,61,66,72,23,17]))