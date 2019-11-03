lens = int(input())
ins  = input()
ind  = [int(x) for x in input().split()]
ans = ''
for i, v in enumerate(ins):
    if i in ind:
        if v.isupper():
            ans += v.lower()
        else:
            ans += v.upper()
    else:
        ans += v
print(ans)

