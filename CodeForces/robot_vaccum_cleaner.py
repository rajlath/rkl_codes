'''
4
ssh
hs
s
hhhs
Output
18
'''
#from sort import sort
def go(st):
    cn, cs = 0
    for i in range(len(st)):
        if st[i]=='s':
            cs += 1
        else:cn += cs
    return cn

def comp(p, q):
    return go(p+q)>go(q+p)

n = int(input())
s = []
for _ in range(n):
    s.append(input())
#s.Sort.sort(cmp=comp)
Sort.sort(s,comp)
print(go("".join(s)))