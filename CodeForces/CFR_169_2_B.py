given = input()
diffs = sum([given.count(i) % 2  for i in set(given)])
print(["Second", "First"][diffs % 2 == 1 or diffs == 0])