a = input()
b = input()

empties = [x.count("0") for x in zip(a, b)]
cnt = 0
can = 0
for emp in empties:
    can += emp
    if can >= 3:
        can -= 3
        cnt += 1
    else:
        can = emp
print(cnt)