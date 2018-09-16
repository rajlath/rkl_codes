'''
Example
Sample Input
9
11 12 8 9 9 2 5 15 16
12

Sample Output
4
'''
from collections import Counter
def count(arr, need):
    arrc = Counter(arr)
    count = 0
    for i in arr:
        curr = need - int(i)
        if curr in arrc:
            count += arrc[curr]
        elif curr - 1 in arrc:
            count += arrc[curr-1]
        elif curr + 1 in arrc:
            count += arrc[curr+1]
        #print(curr, count)
    return count//2


print(count([1, 0, 50, 0, 50, 0, 50, 0, 50, 0],50))


def tester(testname):
    folder = testname+"_tests"
    for i in range(1,51):
        s = str(i)
        if i < 10:s = "0"+str(i)
        infile_name = folder + "\\" +testname+"."+s+"."+"in"
        oufile_name = folder + "\\" +testname+"."+s+"."+"sol"

        in_file = open(infile_name)
        n = int(in_file.readline())
        arr=[int(x) for x in in_file.readline().strip().split()]
        v  = int(in_file.readline())
        #print(arr, v)

        ou_file = open(oufile_name)
        ans  = int(ou_file.readline())
        man  = count(arr, v)
        print(s +" "+ ["Failed", "Passed"][ans == man])
        in_file.close()
        ou_file.close()

#tester("count")
