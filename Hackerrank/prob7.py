'''
b(-1) a(1) b[0] a[2] b[-2] a[-1]
'''
indx = [-1,1,0,2,-2,-1]

a = [x for x in input().split()]
b = [x for x in input().split()]

ans = []
i = len(b)

while True:
    ans.append(b[-1])
    if len(ans)==i:break
    ans.append(a[1])
    if len(ans)==i:break
    ans.append(b[0])
    if len(ans)==i:break
    ans.append(a[2])
    if len(ans)==i:break
    ans.append(b[-2])
    if len(ans)==i:break
    ans.append(a[-1])
    if len(ans)==i:break
print(* ans)


