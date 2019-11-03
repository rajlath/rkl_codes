n, k = [int(x) for x in input().split()]
ins = input()
if n>1:
    ans = "1" + "0" * (n - 1)
else:
    ans = "0"
changed = 0
for i in range(n):
    if ans[i] != ins[i] and changed < k:
        print(ans[i], end='')
        changed += 1
    else:print(ins[i], end='')








