for _ in range(int(input())):
    noe = int(input())
    arr = sorted([int(x) for x in input().split()])
    nos_plus= sum_plus = sum_minus = 0
    for i in range(noe-1, -1, -1):
        if arr[i] <= 0: break
        nos_plus += 1
        sum_plus += arr[i]      
    for j in range(i, -1, -1):
        sum_minus += arr[j]
    ans = (sum_plus * nos_plus) + sum_minus 
    if i == noe - 1:
        print(ans)
    else:
        for j in range(i, -1, -1):
 
            sum_plus+= arr[j]
            sum_minus-= arr[j]
            nos_plus+= 1
 
            temp = (nos_plus*sum_plus) + sum_minus
            ans = max(ans, temp)
        print(ans)
       
       
                
                                
                    
   
