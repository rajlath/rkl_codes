def binary_search(arr, val, l, r):
    while l <= r:
        mid = (l + r)//2
        curr = arr[mid]
        if curr == val:return mid + 1
        elif val < arr[mid]:
            r = mid - 1
        else:l= mid + 1
    return -1

file = open("rosalind_bins.txt", "r")
filw = open("rosalind_bins_ans.txt", "w")
i = 0
for lines in file:
    line = lines.strip()

    if i == 0:
        noe = int(line.strip())
        i += 1
    elif i == 1:
        noq = int(line.strip())
        i += 1
    elif i == 2:
        elem= [int(x) for x in line.split()]
        i += 1
    elif i == 3:
        qury = [int(x) for x in line.split()]
#print(noe, noq, qury,)
'''
noq = int(lines.)
noe = int(input())
noq = int(input())
elem = [int(x) for x in input().split()]
qury = [int(x) for x in input().split()]
'''
res = []
for  i in qury:
    ans = binary_search(elem, i, 0, noe-1)
    print(ans, end=" ", file = filw)


