ins = input()
cnt = 0
if ins[0]=="0":
    cnt = 0
else:
    for i in range(1, len(ins)-1):
        a = ins[:i]
        b = ins[i:]
        
        if b[0] == 0:
            cnt = 0
        else:
            x = b[:len(a)]
            if a == b[:len(a)] and b[-1]=="0":
                cnt += 1
print(cnt)              
        
