given = [x for x in input().strip()]
k1 = int(input().strip())
k2 = int(input().strip())

for i in range(1, 26):
    if (i * (k2)) % 26 == 1:
        k3 = i
        break
decoded = ''
for i in given:
    if i.isupper():
        curr = (((ord(i) - 65) - int(k1)) * int(k3) % 26)
        decoded += chr(curr + 65)
    else:
        curr = (((ord(i) - 97) - int(k1)) * int(k3) % 26)
        decoded += chr(curr + 65)
print(decoded)
