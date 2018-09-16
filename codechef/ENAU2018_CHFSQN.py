def arr_sum(a):
    b = a[1:] + [a[0]]
    return sum([abs(x - y) for x, y in zip(a, b)])

nol = int(input())
arr = [int(x) for x in input().split()]
arrs= sorted(arr)
reord= []
for i in range(nol//2):
    reord.append(arrs[i])
    reord.append(arrs[nol-1-i])
print(arr_sum(reord))
