'''
Problem
Given: A positive integer k≤20, a postive integer n≤104, and k arrays of size n containing integers from −105 to 105.

Return: For each array A[1..n], output three different indices 1≤p<q<r≤n such that A[p]+A[q]+A[r]=0 if exist, and "-1" otherwise.

Sample Dataset
4 5
2 -3 4 10 5
8 -6 4 -2 -8
-5 2 3 2 -4
2 4 -5 6 8
Sample Output
-1
1 2 4
1 2 3
-1
'''
import time
def find_3(a):
    number2indices = {}
    for i in range(len(a)):
        if a[i] not in number2indices:
            number2indices[a[i]] = set()
        number2indices[a[i]].add(i)

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            target = -a[i] - a[j]
            if target in number2indices:
                indices = list(filter(lambda x: x != i and x != j, number2indices[target]))
                if indices:
                    return i, j, indices[0]


ifile = open("rosalind_3sum.txt", "r")
wfile = open("rosalind_3sum_ans.txt", "w")

#
noa, lens = [int(x) for x in ifile.readline().split()]
for z in range(noa):
    #arr  = [int(x) for x in input().split()]
    st = time.time()
    arr  = [int(x) for x in ifile.readline().split()]
    #numbers = {x:i for i,x in enumerate(arr)}
    indices = find_3(arr)
    if indices:
        print(' '.join(map(lambda x: str(x + 1), indices)), file=wfile)
    else:
        print(-1, file=wfile)
    print(time.time() - st)

















