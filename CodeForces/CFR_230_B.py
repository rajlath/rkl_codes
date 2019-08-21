limit = 2 ** 20
valid = []
could_be = [1] * (limit)
for i in range(2, limit):
    if could_be[i]:
        valid.append(i * i)
        for j in range(i * i, limit, i):
            could_be[j] = 0
_ = int(input())
given = [int(x) for x in input().split()]
for i in given:
    print(["NO", "YES"][i in valid])
