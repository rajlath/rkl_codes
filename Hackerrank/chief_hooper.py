'''
5
3 4 3 2 4
'''

import math
input()
h = list(map(int, input().split()))
h.reverse()
energy = 0
for x in h:
  energy = math.ceil((x + energy) / 2)
  print(x, energy)
print(energy) 
