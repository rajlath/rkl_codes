import sys
from collections import Counter
def get_pair_sum(arr, n, sums):
    arrc = Counter(arr)
    twice_count = 0
    for i in range(n):
        twice_count += arrc[sums - arr[i]]
        if sums - arr[i] == arr[i]:
            twice_count -= 1
    return twice_count//2
for i in range(int(input()))        :
    n, k = [int(x) for x in input().split()]
    arr  = [int(x) for x in input().split()]
    print(get_pair_sum(arr, n, k))
