#given an array of signed integer
#find maximum product  of any 3 elements

def find_triplet(arrs):
    n = len(arrs)
    if n < 3: return "wrong input"
    arr = sorted(arrs)

    can = []
    can.append(arr[0] * arr[1] * arr[2])
    can.append(arr[0] * arr[1]* arr[n-1])
    can.append(arr[0] * arr[-2] * arr[-1])
    can.append(arr[-1] * arr[-2]*arr[-3])
    indx = can.index(max(can))

    if   indx == 0: return (arr[0], arr[1], arr[2])
    elif indx == 1: return (arr[0], arr[1], arr[-1])
    elif indx == 2: return (arr[0], arr[-2], arr[-1])
    elif indx == 3: return (arr[-1], arr[-2], arr[-3])

import random
A = [random.randint(-10000, 10000) for _ in range(100)]
#A = [-4, 1,-8,9, 6]
#print(A)
print(find_triplet(A))
