ins = input()
ans = "no"
if len(ins) >= 7:
    for i in range(len(ins)):
        if ins[i] == "1":
            tmp = ins[i:]
            if len(tmp) >= 7 and (len(tmp) - tmp.count("1") + 1 >= 7):
                ans = "yes"
                break 
print(ans)                     
    
        
        
    
