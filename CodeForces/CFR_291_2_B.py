n, x, y = map(int, input().split())
r = set()
for _ in range(n):
    a, b = map(int, input().split())
    if y - b != 0: r.add((x-a)/(y-b))
    else: r.add(2**0.5)
print(r)    
print(len(set(r)))
