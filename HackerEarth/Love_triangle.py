def get_pat(n):
    if n in range(10): return n
    return n%9 + get_pat(n//9)
    
from sys import stdin

lines = stdin.readlines()
for x in lines:
    print(get_pat(x))
