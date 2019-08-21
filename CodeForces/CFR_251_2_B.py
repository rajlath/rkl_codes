subject, hours = [int(x) for x in input().split()]
chapters = sorted([int(x) for x in input().split()])
needed = 0
for i in chapters:
    needed += (hours * i)
    hours = max(hours - 1, 1)
print(needed)
