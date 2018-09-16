def areSimilar(a, b):
    if sorted(a) == sorted(b):
        return sum(x != y for x, y in zip(a, b)) <= 2
    return False



