# D. Dirty Deeds Done Dirt Cheap
nb_pairs = int(input())
bigger, smaller = [], []
for i in range(nb_pairs):
    b = [int(a) for a in input().split()]
    if b[0] > b[1]:bigger.append(b + [i+1])
    else:smaller.append(b + [i+1])
if len(bigger) > len(smaller):
    ans = sorted(bigger)
else:ans = sorted(smaller, reverse=True)
print(len(ans))
print(*[x[2] for x in ans])



