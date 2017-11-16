import re
dicts = []
nops = int(input())
for _ in range(nops):
    ins = input().split()
    if ins[0] == "add":
        dicts.append(ins[1])
        
    elif ins[0] == "find":
        cnt = 0
        to_find = ins[1]
        for i in dicts:
            if i.startswith(to_find):cnt+=1
print(cnt)        
