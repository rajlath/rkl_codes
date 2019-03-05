xs = []
ys = []
for i in range(3):
    x, y  = [int(x) for x in input().split()]
    if x in xs:xs.remove(x)
    else:xs.append(x)
    if y in ys:ys.remove(y)
    else:ys.append(y)
print(xs.pop(), ys.pop())