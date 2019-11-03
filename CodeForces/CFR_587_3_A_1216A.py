lens = int(input())
strs = input()
anss = ''
need = 0
for i in range(0, lens, 2):
    if strs[i] == strs[i+1]:
        need += 1
        anss += ['b','a'][strs[i] == 'b']
        anss += strs[i+1]
    else:
        anss +=   strs[i] +  strs[i+1]
print(need)
print([anss, strs][need==0])
