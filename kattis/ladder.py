from math import sin, ceil
PI = 3.14159265
height , angle = [int(x) for x in input().split()]
rad = angle * (PI / 180)
print(int(ceil(height / sin(rad))))

