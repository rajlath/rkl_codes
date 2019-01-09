R=lambda:[int(x) for x in input().split()]
nb_cases = int(input())
a = [0, 0]
b = [0, 0]

for _ in range(nb_cases):
    server, worked, failed = R()
    if server == 1:
        a[0] += worked
        a[1] += failed
    else:
        b[0] += worked
        b[1] += failed
print("LIVE" if a[0] >= a[1] else "DEAD")
print("LIVE" if b[0] >= b[1] else "DEAD")


