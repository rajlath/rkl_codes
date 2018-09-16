
# -*- coding: utf-8 -*-
# @Date    : 2018-09-10 08:28:00
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

def cpp_upper_bound(arr, n, x):
    """
    implement upper_bound as in cpp
    Returns an iterator pointing to the first element in the range [first,last)
    which compares greater than val.
    type: list arr
    type: n    length of the list
    type: x    value to be adjudged
    rets: int
    """
    left = 0
    rite = n
    while left < rite:
        mid = (left + rite) // 2
        if x >= arr[mid]:
            left = mid + 1
        else:
            rite = mid
    return left

def cpp_lower_bound(arr, n, x):
    """
    implements lower_bound as in cpp
    Returns an iterator pointing to the first element in the range [first, last]
    which does not compare less than val.
    The elements in the range shall already be sorted or at least partitioned with respect to val.

    type: list   arr
    type: int    n  length of the list
    type: int    x  value to be adjudged
    rets: int    p  position of x in the list
    """
    left, rite = 0, n
    while left < rite:
        mid = (left + rite)//2
        if x <= arr[mid]:
            rite = mid
        else:
            left = mid + 1
    return left





import random
lst = sorted(random.sample(range(1, 100), 10))
print(lst)
print(cpp_upper_bound(lst, 10, 56))
print(cpp_lower_bound(lst, 10, 56))


