from collections import Counter
nb_students, nb_question = [int(x) for x in input().split()]
solved = [[x for x in input()] for _ in range(nb_students)]
vals = [max(Counter(x).values()) for x in zip(*solved)]
points = [int(x) for x in input().split()]
print(sum([x * y for x, y in zip(vals,points)]))