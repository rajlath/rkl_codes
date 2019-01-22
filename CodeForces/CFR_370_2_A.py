n = int(input())
crow = [int(x) for x in input().split()] + [0]
was  = []
for i in range(n):
    was.append(crow[i] + crow[i+1])
print(*was)