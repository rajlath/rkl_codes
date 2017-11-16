'''
cat dog hello
stop football play
music is my life


import sys
import string

cef = open("codeeval.txt", "r")
for lines in cef:
	line = lines.strip().split()
	longest = sorted(line, key=len, reverse=True)[0]
	outs = []
	outs.append(longest[0])
	
	for i in range(1, len(longest)):
		outs.append("*" * i + longest[i] )
	print(" ".join(outs))	

(--9Hello----World...--)
Can 0$9 ---you~
13What213are;11you-123+138doing7
|S|DNeysp!v`>)u,48$1QUYH\+Wa

import re
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        ls = re.split(r'[^a-zA-Z]', test.rstrip())
        print(' '.join(e.lower() for e in ls if e))
        
hello 11001
world 10000
cba 111

import sys

cef = open("codeeval.txt", "r")       
for lines in cef:
	a, b = lines.strip().split()
	outs = ""
	for i, v in enumerate(a):
		if b[i]== "1":
			outs += v.upper()
		else:
			outs += v.lower()
	print(outs)	
		

import sys
cef = open(sys.argv[1], "r")
s = [y.split() for y in [x for x in s.split("|")]]
mat = zip(*s)
outs = []
for m in mat:
	m = list(map(int, m))
	outs.append( sorted(m, reverse=True)[0])
print(" ".join(map(str,outs)))
	


import sys
import re
cef = open("codeeval.txt", "r")
for lines in cef:
	maybe, patterns = lines.strip().split("|")
	
	maybe    = maybe.strip()
	patterns = patterns.strip()
	regpat = ".*"
	regpat += '[' + patterns +'].*' 
	regpat *= len(patterns)
	regpat += ".*"
	
	for x in patterns:
		regpat += ".*" + x
	regpat += ".*)"	
	
	maybe = maybe.split()
	wouldbe = []
	for mays in maybe:
		if re.match(regpat, mays):
			wouldbe.append(mays)
	if len(wouldbe) > 0:
		print(" ".join(wouldbe))		
	else:
		print("False")	
			
import sys
from collections import Counter


def isMatch(e, c):
    d = Counter(e)
    print(d)
    return all(d[k] >= v for k, v in c.items())


with open("codeeval.txt", 'r') as test_cases:
    for test in test_cases:
        wines, letters = test.rstrip().split('|')
        c = Counter(letters.strip())
        print(c)
        r = [e for e in wines.split() if isMatch(e, c)]
        if r:
            print(' '.join(r))
        else:
            print('False')
'''

cef = open("codeeval.txt", "r")            
for lines in cef:
	cnts =  [ int(e.split(":")[1]) for e in lines.strip().split(",")]
	noOfHouses = cnts[ -1]
	kids       = cnts[:-1] 	
	totalCandies = [(noOfHouses * kid * val) for kid,val in zip(kids, [3,4,5])] 	
	print(sum(totalCandies)) / sum(kids)
	
	

		
	
	
	
	
	
	
	
