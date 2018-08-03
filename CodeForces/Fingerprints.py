n, m = [int(x) for x in input().split()]
seq  = [int(x) for x in input().split()]
fig  = [int(x) for x in input().split()]
code = []
for i in seq:
    if i in fig:
        code.append(i)
if len(code)>0:
    print(*code)
else:
    print()
