'''
Problem
An inversion of an array A[1..n] is a pair of indices (i,j) such that 1≤i<j≤n and A[i]>A[j]. The number of inversions shows how far the array is from being sorted: if it is already sorted then there are no inversions, whereas if it is sorted in reverse order then the number of inversions is maximal.

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: The number of inversions in A.

Sample Dataset
5
-6 1 15 8 10
Sample Output
2
'''



def merge_sort_inv(arr):
    if len(arr) == 1:return arr,0
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a, ai= merge_sort_inv(a)
        b, bi= merge_sort_inv(b)

        i = 0
        j = 0
        c = []
        inversion = 0 + ai + bi

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversion += (len(a) - i)
    c += a[i:]
    c += b[j:]
    return c, inversion

ifile = open("rosalind_inv.txt", "r")
wfile = open("rosalind_inv_ans.txt", "w")

noe = int(ifile.readline())
arr = [int(x) for x in ifile.readline().split()]
arr, inv = merge_sort_inv(arr)
print(inv, file=wfile)


