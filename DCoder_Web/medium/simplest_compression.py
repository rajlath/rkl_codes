from itertools import groupby
ins = input()
insg = groupby(ins)
lens = len(ins)
answ = ''
for c, v in insg:
    cnt = len(list(v))
    if cnt > 1:
        answ += c + str(cnt)
    else:
        answ += c
if len(answ) < lens:
    print(answ)
else:
    print(ins)
