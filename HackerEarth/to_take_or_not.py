def operation(a, op, b=None):
    if   op == "N" : return -1 *  a
    elif op == "+" : return  a +  b
    elif op == "-" : return  a -  b
    elif op == "*" : return  a *  b
    elif op == "/" : return  a // b
    else:pass
    
    
    
for _ in range(int(input())):
    nops = int(input())    
    mins = maxs = 1
    for i in range(nops):
        ins = [x for x in input().split()]
        curr = [mins, maxs]
        if ins[0] == "N":b=0
        else: b = int(ins[1])
        curr.append(operation(mins, ins[0], b))
        curr.append(operation(maxs, ins[0], b))
        mins = min(curr)
        maxs = max(curr)
    print(maxs)    
            
