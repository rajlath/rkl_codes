n = int(input())
cake = []
t    = 0
for i in range(n):
    cake.append(list(input()))
    x = cake[-1].count("C")
    t += ((x * (x - 1)//2))
for i in zip(*cake):
    x =list(i).count("C")
    t += ((x * (x - 1)//2))
print(t)
