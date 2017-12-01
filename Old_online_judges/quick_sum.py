'''
Source: ACM Mid-Central United States 2006.
IDs for online judges: POJ 3094, ZOJ 2812, UVA 3594.

Quicksum
A checksum is an algorithm that scans a packet of data and returns a single number. The idea
is that if the packet is changed, the checksum will also change, so checksums are often used for
detecting transmission errors, validating document contents, and in many other situations where
it is necessary to detect undesirable changes in data.
For this problem, you will implement a checksum algorithm called quicksum. A quicksum
packet allows only uppercase letters and spaces. It always begins and ends with an uppercase letter.
Otherwise, spaces and letters can occur in any combination, including consecutive spaces.
A quicksum is the sum of the products of each character’s position in the packet times the
character’s value. A space has a value of zero, while letters have a value equal to their position in the
alphabet. So, A = 1, B = 2, and so on, through Z = 26. Here are example quicksum calculations
for the packets “ACM” and “MID CENTRAL”:
Practice for Simple Computing ◾ 19
ACM: 1*1 + 2*3 + 3*13 = 46
MID CENTRAL: 1*13 + 2*9 + 3*4 + 4*0 + 5*3 + 6*5 + 7*14 + 8*20 + 9*18 + 10*1 + 11*12
= 650
Input
The input consists of one or more packets followed by a line containing only # that signals the end
of the input. Each packet is on a line by itself, does not begin or end with a space, and contains
from 1 to 255 characters.
Output
For each packet, output its quicksum on a separate line in the output.
Sample Input Sample Output
ACM 46
MID CENTRAL 650
REGIONAL PROGRAMMING 4690
CONTEST 49
ACN 75
A C M 14
ABC 15
BBC
#

working:
get ordinals of letters and substract 65 if uppercase or 96 if lowercase
space = 0
'''

from string import ascii_uppercase as uc, ascii_lowercase as lc
from sys import stdin, stdout
digs = range(1, 26)
digss = [str(x) for x in range(10)]
ordu = dict(zip(uc,   digs))
ordl = dict(zip(lc,   digs))
di   = dict(zip(digss, digs))
alls = {**ordu, **ordl, **di}
alls[" "] = 0

while True:
    inps = input()
    if inps == "#":
        break
    ans = 0
    for i, v in enumerate(inps):
        ans += alls[v] * (i+1)
    print(ans)







