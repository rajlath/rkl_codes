'''
1
W H
WelloHorld
'''


nos_swap = int(input())
froms = []
tos   = []

for i in range(nos_swap):
    f, t = input().split()
    froms.append(f)
    tos.append(t)


st = (input())

for i in range(nos_swap):
    sw1 = froms[i]+tos[i]
    sw11= "12"

    sw2 = "21"
    sw22= tos[i]+froms[i]



    trantab = str.maketrans(sw1, sw11)
    st1= (st.translate(trantab))

    trantab = str.maketrans(sw2, sw22)
    st = (st1.translate(trantab))


print(st)




