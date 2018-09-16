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
ifile = open("rosalind_2sum.txt", "r")
wfile = open("rosalind_2sum_ans.txt", "w")
nos, lens = [int(x) for x in ifile.readline().split()]
for i in range(nos):
    ans = -1
    arr = [int(x) for x in ifile.readline().split()]
    val = []
    inx = []
    for j in range(lens):
        if arr[j] in val:
            a = j
            b = inx.index(val.index(arr[j]))
            if a > b:
                ans = str(b+1) +" "+str(a+1)
            else:
                ans = str(a+1) +" "+str(b+1)
            break
        else:
            val.append(0-arr[j])
            inx.append(j)
    print(ans, file=wfile)




