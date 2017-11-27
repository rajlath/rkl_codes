i = 1
j = 0
dicts = []
while i < 20:
    curr = "1"*i+"0"*j
    dicts.append(int(curr, 2))
    i+=1
    j+=1



n = int(input())
if n in dicts:print(n)
else:
    for i in range(len(dicts)-1, -1, -1):
        if dicts[i]<n:
            print(dicts[i])
            break

