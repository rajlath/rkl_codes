s = input()
ans=''
for i in s:
    ans += [i.upper(), i.lower()][i.isupper()]
print(ans)