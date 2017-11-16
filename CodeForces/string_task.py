'''
input
tour
output
.t.r
input
Codeforces
output
.c.d.f.r.c.s
input
aBAcAba
output
.b.c.b
'''
s = input()
vowels = "aeiouyAEIOUY"
ans = ""
for i in s:
    if i in vowels:
        continue
    else:
        ans += ("."+i.lower())
print(ans)    