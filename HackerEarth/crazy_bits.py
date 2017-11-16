for _ in range(int(input())):
    n = int(input())
    count=0
    i = 0
    temp = n
    while temp :
        if temp&1:
            count += 1
            temp>>=1
        else:break    
    print(1<<count)   
    res = n ^ 1<< count
    print(res)      

