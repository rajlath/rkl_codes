'''
4
aba
baba
aba
xzxb
3
aba
xzxb
ab
'''
dicts = {}
for i in range(int(input())):
    s = input()
    dicts[s] = dicts.get(s, 0)+1
for i in range(int(input())):
    a = input()
    if a in dicts:
        print(dicts[a])
    else:
        print(0)        