ins = "raj kumar lath bargarh      odissa"
ans = ''
n = len(ins)-1
ans = []
count = i = 0
for i in range(n):
    if not ins[i].isspace():
        ans.append(ins[i])
        count += 1
ans += [" "]*count
print(''.join(ans) + "done")