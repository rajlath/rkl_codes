intab = "aeiou"
outtab = "12345"
trantab = st.maketrans(intab, outtab)

st = "this is string example....wow!!!"
print (st.translate(trantab))
