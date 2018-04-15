import datetime

s = input()
d = int(s[:2])
m = int(s[2:4])
y = int(s[4:8])

print(datetime.date(y,m,d).isoweekday())

abcde
fghij
klmno
pqrst
uvwxy
z