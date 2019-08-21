from string import ascii_uppercase as uc
def first_encryption(s):
    rets = ''
    for i in s:
        rets += uc[::-1][uc.index(i)]
    return rets

encoded = input()
dkey = [x for x in input()]
lens = len(dkey)
offset = len(encoded) // lens
matrix = []
i = 0
for i in range(0,len(encoded), offset):
    if i %2 == 0:
        matrix.append(encoded[i:i+offset])
    else:
        matrix.append(encoded[i:i+offset][::-1])
table = []
for i in dkey:
    table.append(matrix[int(i)])
decoded = list(zip(*table))
encrypt = ''
for i in decoded:
    encrypt += "".join(i)
#encrypt = encrypt[:encrypt.index("X")]
print(first_encryption(encrypt))
