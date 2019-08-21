def KaprekarsConstant(n):
    count = 0
    while n != 6174:
        count += 1
        ns = sorted("0" * ( 4 - len(str(n))) + str(n))
        des = int("".join(ns[::-1]))
        asc = int("".join(ns))
        n = des - asc
    return count

print(KaprekarsConstant(int(input())))



