sl, tl = [int(x) for x in input().split()]
s = input()
t = input()
sa = s.split("*")
ans = "NO"
if len(sa)==2:
    if t.startswith(sa[0]):
        t = t[len(sa[0]):]
        if t.endswith(sa[1]):
            ans = "YES"
print(ans)
