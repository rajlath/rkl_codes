'''
Problem
The merging procedure is an essential part of “Merge Sort”
(which is considered in one of the next problems).

Given: A positive integer n≤10**5 and a sorted array A[1..n] of integers from
−105 to 105, a positive integer m≤105 and a sorted array B[1..m] of integers
from −105 to 105.

Return: A sorted array C[1..n+m] containing all the elements of A and B.

Sample Dataset
4
2 4 10 18
3
-5 11 12
Sample Output
-5 2 4 10 11 12 18
'''
ifile = open("rosalind_mer.txt", "r")
wfile = open("rosalind_mer_ans.txt", "w")

#noeA = int(input())
noeA  = int(ifile.readline())
arrA  = [int(x) for x in ifile.readline().split()]
#arrA = [int(x) for x in input().split()]
noeB  = int(ifile.readline())
#noeB = int(input())
#arrB = [int(x) for x in input().split()]
arrB  = [int(x) for x in ifile.readline().split()]

arr = sorted(arrA + arrB)
#print(len(arr), file=wfile )
for i in arr:
    print(arr[i], end=" ", file = wfile)


'''
i = 0
j = 0
arr = []
while i < noeA and j < noeB:
    if arrA[i] < arrB[j]:
        arr.append(arrA[i])
        i += 1
    else :
        arr.append(arrB[j])
        j += 1

#print(len(arr))
#print(noeA, noeB, i, j )
if i < noeA:
    arr.extend(arrA[i:])
if j < noeB:
    arr.extend(arrB[j:])

print(len(arr), file=wfile)
for i in range(len(arr)):
    print(arr[i], end=" ", file = wfile)

'''