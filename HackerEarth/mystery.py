import sys
from sys import stdin,stdout

    
lines = stdin.readlines()
for line in lines:
    line = int(line)
    print(line&-line)
