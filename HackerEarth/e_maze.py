x, y = 0, 0
ins = input()
for i in ins:
    if   i is "L": x -= 1
    elif i in "R": x += 1
    elif i in "U": y += 1
    elif i in "D": y -= 1
print(x, y)

