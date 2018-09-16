'''
Problem
Given: A positive integer k≤20, a positive integer n≤10**4, and k arrays of size n containing integers from −10**5 to 10**5.
Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if exist, and "-1" otherwise.
Sample Dataset
4 5
2 -3 4 10 5
8 2 4 -2 -8
-5 2 3 2 -4
5 4 -5 6 8
Sample Output
-1
2 4
-1
1 3
'''
import sys
from collections import defaultdict


def binary_search(A, item):
    '''
    Returns item if found in array A,
    otherwise returns -1
    '''
    first = 0
    last = len(A)-1
    found = False
    index = -1

    while first <= last and not found:
        mid = first + (last - first)/2
        if A[mid] == item:
            found = True
            index = mid
        else:
            if item < A[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


def two_sum(A):
    '''
    Takes an array A and returns the two
    indices, if any, if the integer values
    stored at those indices sum to 0
    '''
    two_sums = []
    indices = defaultdict(list)
    for idx in xrange(len(A)):
        item = A[idx]
        if -item in indices:
            two_sum = (indices[-item][0], idx+1)
            two_sums.append(two_sum)
        indices[item].append(idx+1)
    if len(two_sums) is 0:
        return -1
    return two_sums


if __name__ == "__main__":
    filename = "rosalind_2sum.txt"
    with open(filename) as f:
        arrays = [map(int, line.strip().split()) for line in f.readlines()][1:]
        for array in arrays:
            two_sums = two_sum(array)
            if two_sums is -1:
                print -1
            else:
                print two_sums[0][0], two_sums[0][1]