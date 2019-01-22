nb_cabs = int(input())
l, r = 0, 0
for _ in range(nb_cabs):
    a, b = [int(x) for x in input().split()]
    l+= a
    r+= b
print(min(l, nb_cabs-l) + min(r, nb_cabs-r))


