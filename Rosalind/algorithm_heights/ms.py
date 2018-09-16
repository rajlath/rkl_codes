'''
Merge Sort
Problem
The problem of sorting a list of numbers lends itself immediately to a divide-and-conquer strategy: split the list into two halves, recursively sort each half, and then merge the two sorted sublists (recall the problem “Merge Two Sorted Arrays”).

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A sorted array A[1..n].

Sample Dataset
10
20 19 35 -18 17 -20 20 1 4 4
Sample Output
-20 -18 1 4 4 17 19 20 20 35
'''
def merge(a, b):
    c = []
    ia, ib = 0, 0
    while ia < len(a) or ib < len(b):
        if ia < len(a) and (ib == len(b) or a[ia] <= b[ib]):
            c.append(a[ia])
            ia += 1
        else:
            c.append(b[ib])
            ib += 1
    return c

def merge_sort(arr):
    size = len(arr)
    if size < 2: return arr
    return merge(merge_sort(arr[:size//2]), merge_sort(arr[size//2:]))

#lens = int(input())
#arrs = [int(x) for x in input().split()]
ifile = open("rosalind_ms.txt", "r")
wfile = open("rosalind_ms_ans.txt", "w")
lens = int(ifile.readline())
arrs = [int(x) for x in ifile.readline().split()]
ans = merge_sort(arrs)
print(*ans, file= wfile)
