for i in range(int(input())):
    s, e  = [int(x) for x in input().split()] 
    if e - s == 1:print(e & s)
    elif e and (not(e & (e-1))):print(e-2)
    else:print([e-2, e-1][e%2])
    
    
