lens = int(input())
arrs = [int(x) for x in input().split()]
i = 0
while i < lens:
    arrs[i], arrs[lens - 1] = arrs[lens - 1], arrs[i]
    i += 2
    lens -= 2
print(*arrs)    
