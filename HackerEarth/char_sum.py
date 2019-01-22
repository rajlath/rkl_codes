from string import ascii_lowercase as al
weights = dict(zip(al, range(1, 27)))
print(sum([weights[x] for x in input()]))