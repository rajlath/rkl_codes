nob, noo, here = [int(x) for x in input().split()]
for i in range(noo):
    s1, s2 = [int(x) for x in input().split()]
    if s1==here:here=s2
    elif s2==here:here=s1

print(here)
