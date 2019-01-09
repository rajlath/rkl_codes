seq = []
indx = 0
for i in range(1, 1001):
    curr = str(i)
    for j in curr:
        seq.append(j)
        indx += 1
print(seq[int(input()) - 1])

