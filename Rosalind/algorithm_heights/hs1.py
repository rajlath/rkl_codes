'''
Problem
The heap sort algorithm first transforms a given array into a max heap (recall the problem “Building a Heap”).
It then repeats the following two simple steps n−1 times:

Swap the last element of the heap with its root and decrease the size of the heap by 1.
"Sift-down" the new root element to its proper place.
Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A sorted array A.

Sample Dataset
9
2 6 7 1 3 5 4 8 9
Sample Output
1 2 3 4 5 6 7 8 9
'''
def move_down(lst, first, last):
    largest = 2 * first + 1
    while largest <= last:
        if largest < last and arr[largest] < arr[largest + 1]:
            largest += 1
        if arr[largest] > arr[first]:
            arr[largest], arr[first] = arr[first], arr[largest]
            first = largest
            largest = 2 * first + 1
        else:
            return

ifile = open("rosalind_hs.txt", "r")
wfile = open("rosalind_hs_ans.txt", "w")
noe = int(ifile.readline())
arr = [int(x) for x in ifile.readline().split()]
lens = len(arr) - 1
lparent = lens // 2
for i in range(lparent, -1, -1):
    move_down(arr, i, lens)
for i in range(lens, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    move_down(arr, 0, i-1)
print(*arr, file=wfile)



