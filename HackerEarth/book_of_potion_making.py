isbn = [int(x) for x in input()]
sums = 0
for i, v  in enumerate(isbn):
    sums += (i+1) * v
print(["Illegal ISBN","Legal ISBN"][sums%11== 0])