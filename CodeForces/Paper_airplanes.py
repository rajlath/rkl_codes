'''
inputCopy
5 3 2 3
outputCopy
4
inputCopy
5 3 100 1
outputCopy
5
'''

from math import  ceil
person, plane, persheet, perpack = [int(x) for x in input().split()]
each_person_need = ceil(1 / persheet * plane)
pack_needed = ceil(1 / perpack * (each_person_need * person))
print(pack_needed)

