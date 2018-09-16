#given an array of signed integer
#find number of ways to arrive at a target
#by only adding or subtracting elements of the array

def get_target(arr,n, target):

    if target == 0:return 1
    if n == 0     :return 0
    exclude = get_target(arr, n, target)
    include = get_target(arr, n, target - arr[n]) + get_target(arr, n, target + arr[n])
    return exclude + include

import random
A = [random.randint(-100, 100) for _ in range(10)]
A = [5,3-6,2]
#print(A)
print(get_target(A, len(A)-1,6))
