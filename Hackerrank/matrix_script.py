from string import ascii_letters, digits

valids = ascii_letters + digits
n, m = [int(x) for x in input().split()]
codes= []
for _ in range(n):
    codes.append([x for x in input()])
dcode = [[row[i] for row in codes] for i in range(len(codes[0]))]
decode = ""
for i in range(len(dcode)):
    decode += ''.join(dcode[i])
decoded = ''
for i in decode:

    if i in valids:
        decoded += i
    else:
        try:
            if decoded[-1]  in valids:
                print(decoded[-1], i)
                decoded += " "
        except IndexError:
            print(decoded)


print(decoded)

