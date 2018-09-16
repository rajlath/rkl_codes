intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "zyxwvutsrqponmlkjihgfedcba"
trantab = str.maketrans(intab, outtab)

for _ in range(int(input())):
    lena = int(input())
    ins  = list(input())
    limit = lena - 1
    if limit%2==0:limit = limit - 1
    #print(limit)
    i = 0
    while i < limit:
        ins[i], ins[i+1] = ins[i+1], ins[i]
        i += 2
    ins = "".join(ins)
    #print(ins)
    print(str.translate(ins, trantab))



