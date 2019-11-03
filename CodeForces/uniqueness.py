lens = int(input())
arrs = [int(x) for x in input().split()]
unique = []
unindex = []
for i, v in enumerate(arrs):
    if v not in unique:
        unique.append(v)
        continue
    else:
        unindex.append(i)
print(unindex)
if len(unindex) < 2:
    print(len(unindex))
else:
    answer = unindex[-1] - unindex[0]
    if answer == 1: answer += 1
    print(answer)




