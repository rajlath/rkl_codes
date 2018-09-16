'''
Sample Dataset
6
6 10 4 5 1 2
Sample Output
12
'''
#noe = int(input())
#arr = [int(x) for x in input().split()]
ifile = open("rosalind_ins.txt", "r")
ofile = open("rosalind_ins_ans.txt", "w")
noe = int(ifile.readline())
arr = [int(x) for x in ifile.readline().split()]
swapped = 0
for i in range(1, noe):
    k = i
    while arr[k] < arr[k-1] and k > 0:
        arr[k], arr[k-1] = arr[k-1], arr[k]
        k -= 1
        swapped += 1
print(swapped)


