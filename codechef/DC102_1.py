encoded = input().strip()
keys = [int(i) for i in input()]
rows = len(encoded) // len(keys)
rbegin = 0
rend = rows

mat = []
for i in range(len(keys)):
    if i % 2:
        mat.append(encoded[rbegin:rend][::-1])
    else:
        mat.append(encoded[rbegin:rend])
    rbegin = rend
    rend += rows
mat2 = []
for i in keys:
    mat2.append(list(mat[i]))
en = ''
for i in range(rows)   :
    for j in mat2:
        en += j[i]
decoded = ''
for i in en:
    if ord(i) <= 77:
        x = 77 - ord(i) + 1
        decoded += chr(x + 77)
    else:
        x = 90 - ord(i)
        decoded += chr(65 + x)
print(decoded)
