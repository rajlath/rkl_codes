
'''
mins = 0
maxs = 0
events = []
for i in range(nb_events):
    a, b = [int(x) for x in input().split()]
    events.append((a, b))
    mins = min(mins, a, b)
    maxs = max(maxs, a, b)
days = [0 for i in range(maxs + 1)]
for i in events:
    a, b = i
    for x in range(a, b+1):days[x] = 1
print(sum(days))
'''
nb_events = int(input())
days = set()
for _ in range(nb_events):
    a, b = [int(x) for x in input().split()]
    for i in range(a, b+1):
        days.add(i)
print(len(days))


