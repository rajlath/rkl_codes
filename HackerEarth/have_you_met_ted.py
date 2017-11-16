for _ in range(int(input())):
    input()
    arr = [int(x) for x in input().split()]
    mins = 100
    for i in arr:
        c = 0
        while(i):
            c+= (i&1)
            i>>=1
        mins = min(mins, c)    
    print(mins)    
