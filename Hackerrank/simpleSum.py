k, a, b = [int(x) for x in input().split()]
mod = int(10 ** 9 + 7)

vals = []
x = b
i = 0
while True:
    x =   (k * i) +(i + 1)
    if x < b:
        vals.append(x)
    else:break
    i += 1
vals.append(b - vals[-1])
print(vals)

x   =  0
cnts = k
sums = 0
for i in range(len(vals)):
    cnts = (i * vals[i] + (i+1))%mod
    if cnts < a:
        sums += (((cnts - k) + 1) * vals[i])%mod
    else:
        sums += ( cnts * vals[i])%mod
print(sums)







