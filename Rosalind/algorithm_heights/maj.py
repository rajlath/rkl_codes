'''
http://rosalind.info/problems/maj/
Problem
An array A[1..n] is said to have a majority element if more than half of its
entries are the same.
Given: A positive integer k≤20, a positive integer n≤10**4, and k arrays
of size n containing positive integers not exceeding 105.

Return: For each array, output an element of this array occurring strictly
more than n/2 times if such element exists, and "-1" otherwise.
Sample Dataset
4 8
5 5 5 5 5 5 5 5
8 7 7 7 1 7 3 7
7 1 6 5 10 100 1000 1
5 1 6 7 1 1 10 1
Sample Output
5 7 -1 -1
'''
ifile = open("rosalind_maj.txt", "r")
wfile = open("rosalind_maj_ans.txt", "w")
#noq, noe = [int(x) for x in input().split()]
noq, noe  = [int(x) for x in ifile.readline().split()]
for i in range(noq):
    #arr  = sorted([int(x) for x in input().split()])
    arr  = sorted([int(x) for x in ifile.readline().split()])
    ans  = arr[noe//2]
    if arr.count(ans) > noe//2:
        print(ans,file=wfile)
    else:print(-1, file = wfile)

