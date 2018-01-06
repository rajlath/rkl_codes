'''
Input:
3
1
1 2
3
1 2 3 4 5 6
3
1 3 3 3 2 2

Output:
2
1 2
5
1 3 2 5 4 6
3
1 3 3 3 2 2
'''
for _ in xrange(int(raw_input())):
    n = int(raw_input())
    arr = sorted(map(int, raw_input().split()))
    print arr[3*n/2]
    res = 2*n*[0]
    for i in xrange(0,2*n,2):
        res[i] = arr[i/2]
        res[i+1] = arr[n+i/2]
    print str(res)[1:-1].replace(',', '')


