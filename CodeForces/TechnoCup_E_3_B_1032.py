import math
line = input()
rows = math.ceil(len(line) / 20)
cols = math.ceil(len(line) / rows)
stars= rows * cols - len(line)
print(rows, cols)
c = 0
for  i in range(rows):
    r = 1 if stars > 0 else 0
    used = cols - r
    print("*" * r + line[c:c + used])
    stars -= r
    c += used

