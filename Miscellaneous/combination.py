import itertools

for x in itertools.product('12', repeat=3):
    w = ''.join(x)
    print( w)
