'''
9
110011101

from itertools import groupby
noc = int(input())

arlist = [list(g) for k, g in groupby(input())]
out = ""
for i in arlist:
    if i[0] == "1":
        out += str(len(i))
    elif i[0] == "0":
        if len(i)>1:
            out += "0"*(len(i)-1)
print(out)            
'''        
i=input;i();print(''.join(map(str,map(len,i().split('0')))))
