from math import pi, sin
nb_outer, inner_radius = [int(x) for x in input().split()]
outer = pi / nb_outer
outer = sin(outer)
print(outer * inner_radius / (1 - outer))
