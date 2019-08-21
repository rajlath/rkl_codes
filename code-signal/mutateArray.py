def mutateTheArray(n, a):
    b = []
    for i in range(n):
        if i == 0:
            b.append(a[i] + a[i + 1])
        elif i == n - 1:
            b.append(a[i-1] + a[i])
        else:b.append((a[i - 1] + a[i] + a [i + 1]))
        #b.append(curr)
    return b

print(mutateTheArray(5, [4, 0, 1, -2, 3]))
