nol = int(input())
a = list(input())
b = list(input())
i, j = 0, 0
for i in range(nol):
    if a[i] == b[i]:continue
    else:
        j = i
        while a[j] != b[i] and j < nol:
            a[j], a[j+1] = a[j+1], a[j]
            if a[j] == b[i]:
                break
            j += 1
        print(i+1)
print(a, b)




