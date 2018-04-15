n, limit = [int(x) for x in input().split()]
arr = []
for i in range(n):
    arr.append(int(input()))
sums = sum(arr)
alls = 0
valid= 0
for i in range(n):
    for j in range(i, n):
        alls += 1
        if sum(arr[i:j+1])<=limit:valid+=1
print("%0.6f" % (valid/alls))



