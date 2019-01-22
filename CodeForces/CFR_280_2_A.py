n = int(input())
total =  row = 1
while n > 0:
    row += 1
    total += row
    n -= total
    print(row, total)
print(row - 1)


