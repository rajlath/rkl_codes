a, b = [int(x) for x in input().split()]
answ = -1
for i in range(a, b+1):
    curr = str(i)
    if len(curr) == len(set(curr)):
        answ = i
        break
print(answ)
