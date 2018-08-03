maxall = 0
for _ in range(int(input())):
    curr = input().split()
    val  = int(curr[1])
    if curr[0] == "add":
        if maxall+val > maxall:
            maxall = maxall + val
    else:
        if val > maxall:
            maxall = val
print(maxall)
