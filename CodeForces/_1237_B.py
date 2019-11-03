lens = int(input())
ins  = [int(x) for x in input().split()]
out  = [int(x) for x in input().split()]
fined = 0
for x, y in zip(ins[::-1], out):
    print(x, y)
    fined += x != y
print(fined)

