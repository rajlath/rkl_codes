q = []
for _ in range(int(input())):
    arr = input().split()
    if len(arr)==1 :
        if len(q)>=1:            
            s = q.pop(0)
            print(s,len(q))
        else:
            print(-1, len(q))
    else:
        q.append(arr[1])
        print(len(q))
        
