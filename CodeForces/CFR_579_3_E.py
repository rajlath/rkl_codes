n = int(input())
a = sorted([int(x) for x in input().split()])
s = set()
for i in a:
    if i > 1 and i - 1 not in s:s.add(i - 1)
    elif i not in s: s.add(i)
    elif i + 1 not in s: s.add(i + 1)
print(len(s))
