'''
3
10
1 3 7 2 5 1 4 2 1 5
5
1 1 1 1 1
6
1 1 2 2 2 3
'''
from collections import Counter
for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    arrc = Counter(arr)
    
    stack = []
    idx = []
    ans = [-1] * noe
    
    for i in range(noe):
        if not stack:
            stack.append(arr[i])
            idx.append(i)
        else:
             while(arrc[arr[i]]>arrc[stack[-1]]):
                 stack.pop()
                 ans[idx.pop()]=arr[i]
                 if not stack : break
             stack.append(arr[i])
             idx.append(i) 
    print(" ".join(map(str, ans)))            
                 
                
    
        
        
'''             
    
    t=int(input())
for i in range (t):
    n=int(input())
    a=[]
    a.extend(map(int,input().split()))
    f={}
    for j in a:
        try:
            f[j]+=1
        except:
            f[j]=1
    s=[]
    ind=[]
    ans=[]
    for j in range (n):
        ans.append(-1)
    for j in range (n):
        if(len(s)==0):
            s.append(a[j])
            ind.append(j)
        else:
            while(f[a[j]]>f[s[-1]]):
                s.pop()
                ans[ind.pop()]=a[j]
                if(len(s)==0):
                    break
            s.append(a[j])
            ind.append(j)
    for i in ans:
        print(i,end=" ")
    print()
'''    
