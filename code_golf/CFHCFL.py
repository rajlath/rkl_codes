'''
Example:

Input:
2
5
6 14 18 51 54
100
4
103 110 140 148
50

Output:
yes
no
'''
from math import floor
def is_even_parity(n):
    return bin(n)[2:].count("1")%2==1

for _ in range(int(input())):
    noe = int(input())
    arr = [int(x) for x in input().split()]
    men = sum(arr)
    adds=int(input())
    mins= floor(men/noe)
    xor1=mins^adds
    if xor1 >= mins and is_even_parity(adds):
        print("yes")
    else:
        print("no")


