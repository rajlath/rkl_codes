from functools import reduce
print( (lambda k: reduce(int.__mul__, range(1,k+1), 1))(int(input())) )