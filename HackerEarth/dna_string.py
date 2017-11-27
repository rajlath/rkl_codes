

ins = "ATCG"
out = "TAGC"
trans = "".maketrans(ins, out)
for _ in range(int(input())):
    input()
    s = input()
    if any([x for x in s if x not in ins]):
        print("Error RNA nucleobases found!")
    else:
        print(s.translate(trans))