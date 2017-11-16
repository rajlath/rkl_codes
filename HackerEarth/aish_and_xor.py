noe = int(input())
arr = [int(x) for x in input().split()]
arr = [0] + arr

    

qry = int(input())    
for _ in range(qry):
    l, r = [int(x) for x in input().split()]
    xors = 0
    cnt = 0
    for i in range(l, r+1):
        xors = xors ^ arr[i]
        cnt += arr[i]==0
    print(xors, cnt)    
