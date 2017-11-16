def rotate_left(st, times=1):
    lens = len(st)
    rets =""
    for i in range(lens):
        rets += st[(i+1)%lens]
    return rets    
        
for i in range(int(input())):
    rotate = int(input())
    bstr = input()    
    
    cnt = 0 
    for d in range(rotate):        
        bstr = rotate_left(bstr)
        
        cnt += int(bstr, 2)%2==0
    print(cnt)    
        
        
        


