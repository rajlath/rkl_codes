a = [5,2, 9, 5, 2, 3, 5]
maxs = max(a) + 1
sorted_a = [0] * (len(a)+1)
aux  = [0] * (maxs)
for i in a:
    aux[i] += 1
j = 0
for i in range(maxs):
    curr = aux[i]
    while curr:
        #print(j)
        sorted_a[j] = i
        j += 1
        curr -= 1
print(sorted_a[:len(a)])
