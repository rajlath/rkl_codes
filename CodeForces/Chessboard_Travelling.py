from math import factorial
import re

def get_numbers(s):
    pats = re.compile(r'(\d+)')
    return [int(x) for x in re.findall(pats, s)]



def ChessboardTravelling(s):
    sx, sy, ex, ey = get_numbers(s)
    up    = ex - sx
    right = ey - sy

    return (factorial(up + right) // (factorial(up) * factorial(right)))



print(ChessboardTravelling("(1 1)(3 3)"))


'''
up = pos[1][0] - pos[0][0]
    right = pos[1][1] - pos[0][1]

    return math.factorial(up + right)/(math.factorial(up) * math.factorial(right))

# keep this function call here
print ChessboardTraveling(raw_input())
'''
