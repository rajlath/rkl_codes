for _ in range(int(input())):
    plain = input()
    enc   = input()
    valid= True
    offset = (ord(enc[0]) - ord(plain[0]))
    if offset < 0:
        offset = offset + 26
    elif offset > 25:
        offset = offset - 25

    for i in range(1, len(plain)):
        offset1 = (ord(enc[i]) - ord(plain[i]))
        if offset1 < 0:
            offset1 = offset1 + 26
        elif offset1 > 25:
            offset1 = offset1 - 25
        if offset1 != offset:
            valid = False
            break
    print(-1 if not valid else offset)
'''
5
GX
PU
MKXKSZH
BPPHYKI
KEZPLVFJ
QMOPODOT
RJZRIML
LDTLCGF
U
R

-1
-1
-1
6
3

-1
-1
-1
20
23
'''