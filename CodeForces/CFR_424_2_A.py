s = input()
t = input()
maps = dict(zip(s, t))
decoded = ''
encoded = input()
for i in encoded:
    if i.lower() in maps:
        if i.isupper():
            decoded += maps[i.lower()].upper()
        else:
            decoded += maps[i.lower()]
    else:
        decoded += i


print(decoded)
