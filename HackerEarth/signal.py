for i in range(int(input())):
    
    noe = int(input())
    ans = [None] * noe
    arr = [int(x) for x in input().split()]
    stk = []
    for i in range(noe-1, -1, -1):
        while(len(stk)>0 and arr[i]>=arr[stk[-1]]):
            ans[stk[-1]] = i
            stk = stk[:-1]
        stk.append(i)    
    while (len(stk)>0):
        ans[stk[-1]] = -1
        stk = stk[:-1]
       
    for i in range(noe):
        print("%d" % (i-ans[i]), end = " ")
    print()    
        
            
	           
