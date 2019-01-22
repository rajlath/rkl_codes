ins = input()
ans = ''
for i in ins:
    if i.isupper():
        ans += i.lower()
    else:
        ans += i.upper()
print(ans)