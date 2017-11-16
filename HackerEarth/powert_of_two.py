def pow_2(num):
    return  num and (not(num&(num-1)))
    
total = 0
for i in range(32):
    tmp = 1<<i    
    total += tmp
    
for _ in range(int(input()))    :
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n == 1:
        if pow_2(arr[0]):
            print("YES")
        else:
            print("NO")
        continue 
               
    flag = False    
    for i in range(32):
        ans  = total
        for j in range(n):
            if arr[j]&(1<<i):
                ans&=arr[j]
            if pow_2(ans):
                flag = True
                break
    print("YES" if flag else "NO")                
        
        
                
   




