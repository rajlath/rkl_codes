a,b=[int(x) for x in input().split()];f=[0,1];
for i in range(b):f.append(f[-1]+f[-2])
x=f[b-1]

