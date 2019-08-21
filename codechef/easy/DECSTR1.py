from string import ascii_lowercase as lc
lc = list(reversed(lc))
fulls = "".join(lc)
for _ in range(int(input())):
    pos = int(input())
    full, rems = divmod(pos, 25)
    ans = ''
    if rems > 0:
        ans += "".join(lc[-rems - 1:])
    for i in range(full):
        ans += fulls
    print(ans)
