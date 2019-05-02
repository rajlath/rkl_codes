N, T = [int(x) for x in input().split()]
mins = int(-1e9)
maxs = int(1e9)

dist= []
speed=[]
for i in range(N):
    d, s = [int(x) for x in input().split()]
    dist.append(d)
    speed.append(s)
    mins = max(mins, -s)

while maxs - mins > int(1e-9):
    c = (maxs + mins) / 2
    t = 0.0
    for i in range(N):
        t += dist[i] / (speed[i] + c)
        if t > T:
            mins = c
        else:
             maxs = c
print("{:.9}".format((maxs + mins) / 2))