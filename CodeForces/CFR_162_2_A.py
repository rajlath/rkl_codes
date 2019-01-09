s = " "+input()
t = input()
pos = 1
for i, v in enumerate(t):
    if s[pos] == v:pos+=1
print(pos)