r=range
for i in r(1,101):
    c=[1]
    for j in r(2,i+1):
        if not i%j:c.append(j)
print(*c)