s = input()
k = len(set(s))
ss= list(set(s))
ans="NO"
if k == 4 or k==3 and len(s)!=3 or k==2 and s.count(ss[0])!=1 and s.count(ss[1])!=1:
    ans = "YES"
print(ans)