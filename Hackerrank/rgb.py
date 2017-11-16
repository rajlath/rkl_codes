import re
for _ in range(int(input())):
    s = input()
    rp = re.compile(r"\#[0-9a-fA-F]{3,6}")
    if s.startswith("#"):
        continue
    else:
        res = re.findall(rp, s)
        if len(res)>0:
            for i in res:
                print(i)   
        
        
