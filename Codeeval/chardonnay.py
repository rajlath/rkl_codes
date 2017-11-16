import sys
import re
from itertools import permutations

with open("chardonnay.txt","r") as cef:
    for line in cef.readline():
        print(line)        
        names, hehave = line.split('|')
        names = names.split()
        found = [j for j in names if
             any(re.search('.*?'.join(i), j) for i in permutations(hehave))]
        print(" ".join(found) if found else "False")
