from string import ascii_lowercase as lc
nb_line, dicts = input().split()
nb_line = int(nb_line)
for _ in range(nb_line):
    current = input()
    trans   = ''
    for i in current:
        if i == "_":
            trans += " "
        else:
            if i.isalpha():
                if i.isupper():
                    trans += dicts[lc.index(i.lower())].upper()
                else:
                    trans += dicts[lc.index(i.lower())]

            else:
                trans += i
    print(trans)
