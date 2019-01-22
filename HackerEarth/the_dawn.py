ins = int(input())
sqt = int(ins ** 0.5)
while ins % sqt != 0:
    sqt -= 1
B = ins // sqt
print(sqt + B)