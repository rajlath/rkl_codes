x = int(input())
for i in [2, 3, 5]:
    m, d = divmod(x, i)
    if d in [2, 3, 5]:
        print(str(i)*m,d)
    if d ==0:
        print(str(i)*m)
