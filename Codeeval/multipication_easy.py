'''
for i in range(1, 13):
	curr = []
	for j in range(1, 13):
		mult = i * j
		mults = '{:>4}'.format(mult)
		curr.append(mults)		
	print("".join(curr))
	
		
cef = open("codeeval.txt", "r")	
lines = cef.readlines()
ans = 0
for line in lines:
	ans += int(line)
print(ans)	

odds = [x for x in range(1,100) if x&1!=0]
print("\n".join(map(str,odds)))

import os
cef = open("codeeval.txt", "r")
print(os.fstat(cef.fileno()).st_size)


print(" ".join(map(str,sorted(list(set([1,1,1,2,2,3,3,4,4]))))))

cef = open("codeeval.txt", "r") 
for lines in cef:
	setA, setB = lines.split(";")
	setA, setB = set(map(int, setA.split(","))), set(map(int, setB.split(",")))
	ans = setA.intersection(setB)
	print(",".join(map(str, ans)))


import re
import sys

with open("codeeval.txt", 'r') as test_cases:
    for test in test_cases:
        src,tofind  = test.split(",")        
        fnd = list([x.start() for x in re.finditer(str(tofind.strip()), src)])
        ans = "-1"
        if fnd:ans = "".join(map(str,fnd[-1:]))
        print(ans)
	

	
def isHappy(n, done):
	if n == 1:
		return 1
	if n in done:
		return 0
	done.append(n)	
	n = sum([int(x)*int(x) for x in str(n)])	
	return isHappy(n ,done)
	


done = []
cef = open(input(), "r")
for lines in cef:
	n = int(lines.strip())
	print(isHappy(n, done))

from collections import Counter
import sys

cef = open(input(), "r")
for lines in cef:
	nc = dict(Counter(lines.strip()))		
	ans = "1"
	inc = {}
	for i, v in enumerate(lines.strip()):
		if v == '0':
			continue
		else:
			inc[str(i)]	= int(v)		
	check = set(nc.items()) ^ set(inc.items())		
	print("0" if check else "1")
		
	

	

n = "2020"
ans = "1"
for i, v in enumerate(n):
	if nc[i]!=v:
		ans = "0"
		break
print(ans)	

print(int("9f",16))

import sys

def getArms(n):
	lens = len(n)
	return sum(map(lambda e: int(e)**lens, n)) == int(n)
		
	

with open(input(), 'r') as test_cases:
	for test in test_cases:
		print(getArms(test.strip()))
		
from collections import Counter	



def calculateBeauty(she)		:
	she = Counter(she.lower())
	shedicts = she.most_common()	
	score = 26
	beauty = 0
	for k, v in shedicts:
		if  k >= "a" and k <= "z":
			beauty += score * v
			
			score-=1
	return beauty
	
cef = open(input(),"r")		
for lines in cef:	
	
	
matrix = [[0]*256]*256
cef = open(input(), "r")
for line in cef:
	line = line.strip().split(" ")	
	if len(line) == 3:		
		opcode, a, b = line[0].strip(), int(line[1]), int(line[2])
		if opcode == "SetCol":
			for i in range(256):
				matrix[i][a] = b			
		if opcode == "SetRow":
			for i in range(256):
				matrix[a][i] = b
	if len(line) == 2:		
		opcode, a = line[0].strip(), int(line[1])
		if opcode == "QueryCol":
			sums = 0
			for i in range(256):
				sums += matrix[i][a]
			print(sums)	
		if opcode == "QueryRow":
			print(sum(matrix[a]))
print(calculateBeauty(lines.strip()))
		
import sys

with open(input(), 'r') as test_cases:
    for test in test_cases:
        arr = map(float, test.strip().split(" "))
        arr = sorted(arr)        
        print(" ".join(map(lambda x: "%.3f" % (x), arr)))	
        			
				
		
		 
with open(input(), "r") as cef:
	for lines in cef:
		words  = lines.strip().split()
		news = []
		for i in words:
			news.append(i[0].upper() + i[1:])
		print(" ".join(news))


line = "osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg| 3 35 27 62 51 27 46 57 26 10 46 63 57 45 15 43 53"		
key, indx = line.strip().split("|")
indx = indx.lstrip()
ind = [x for x in indx.split(" ") if x != " "]
ans = ""
for i in ind:
	
	ans += key[int(i)-1]
print(ans)	

import re

x = "(47, 43) (-25, -11)"
x1 = re.findall("([-]*\d+)", x)	
p1x,p1y,p2x,p2y = map(int, x1)	
print(int(((p2x -p1x)*(p2x - p1x) + (p2y -p1y)*(p2y - p1y)) ** 0.5))

if 702 & 1 :
	print("odd")
else:
	print("even")	
	

import json

def getTotal(item):
	totals = 0
	for x in items:
		totals += x["id"]
	return totals		
	

dicts = u'{"menu": {"header": "menu", "items": [{"id": 27}, {"id": 0, "label": "Label 0"}, null, {"id": 93}, {"id": 85}, {"id": 54}, null, {"id": 46, "label": "Label 46"}] }}'

import json
with open(input(), "r") as cef:
	for lines in cef:
		if lines == "":continue
		dicts = json.loads(lines.strip())
		items = dicts["menu"]['items']
		items = [a for a in items if a!=None]
		sums = 0
		for item in items:
			if len(item)>1:
				if "id" in item and "label" in item:
					sums += item["id"]
		print(sums)
					
from collections import Counter
with open(input(), "r") as cef:
	for lines in cef:
		score = list(map(int, lines.strip().split(" ")))
		scores = Counter(score).most_common()
		mins = None
		
		for k, v in scores:
			if v > 1: continue
			
			if mins == None:
				mins=k
			else:
				mins = min(mins, k)	
			
		print("0" if mins==None else score.index(mins) + 1)	

digwords = ["zero","one", "two","three","four","five","six","seven","eight", "nine"]		
digdic   = dict(zip(digwords, ["0","1","2","3","4","5","6","7","8","9"]))
cef = open(input(), "r")
for lines in cef:
	line = lines.strip().split(";")
	ans = ""
	for ln in line:
		ans += digdic[ln.strip()]
	print(ans)	
	
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))
                   
def toRoman(n):
    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result  

print(toRoman(3992))   


print(sorted("some line with text once".split(" "), key = len)[0])

cef = open(input(), "r")
for lines in cef:
	series , exchanges = lines.strip().split(":")
	series = list(map(int, series.strip().split(" ")))
	exchanges = exchanges.split(",")
	exchanges = [x.rstrip().lstrip() for x in exchanges]
	for exchange in exchanges:
		a, b = map(int, exchange.split("-"))
		series[a], series[b] = series[b], series[a]
	print(" ".join(map(str, series)))	
 

cef = open(input(), "r")	
for lines in cef:
	listA, listB = lines.strip().split("|")
	listA = listA.strip().split(" ")
	listB = listB.strip().split(" ")
	listA = [int(x) for x in listA]
	listB = [int(x) for x in listB]
	mult  = [(x * y) for (x, y) in zip(listA, listB)]

import re
import sys

cef = open(input(), "r")
for lines in cef:	
    lines = lines.strip().split(",")
    alphs, digits = [], []
    for line in lines:
        if re.match("\d+", line.strip()):
            digits.append(line.strip())
        else:
            alphs.append(line.strip())
    if len(alphs)==0 or len(digits)==0:
        print(lines)
    else:
        print("%s|%s" % (','.join(alphs), ','.join(digits)))        
        

def two_sum():
	l = [2, 11, 15, 23, 42, 11, 8, 45, 7]
	target = 9
	return [(l.index(l[i]), l.index(l[i+1]))for i in range(0,len(l)-1) if sum([l[i],l[i+1]]) == target][0]

print (two_sum())


def make_change(coins, n):
    lookup = [1] + [0] * n
    print(lookup)
    for coin in coins:
        for i in range(n+1-coin):
            lookup[i+coin] += lookup[i]
            print(lookup)
    return lookup[n]
    

def find_staircase_dp(n):
    table=[]
    #insert base case
    table.insert(0,1);
    table.insert(1,1);
    table.insert(2,2); #(1,1|2) 2 ways 
    table.insert(3,4); #(1,2| 1,1,1|2,1|3) 4 ways 
    #Iterate if N >= 4
    for i in range(4,n+1):
        val = table[i-1] + table[i-2] +table[i-3]
        table.insert(i,val);
        print(table)
    return table[n]
s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(find_staircase_dp(n))
 print(make_change([1,2,3], 4))   


valid_letters = ["a","b","c","d","e","f","g","h","i","j"]
to_index      = dict(zip(valid_letters, range(10)))

print(to_index)
cef = open(input(), "r")
for lines in cef:
	lines = lines.strip()
	ans = ""
	for ch in lines:
		try:
			chi = int(ch)
			ans += ch
		except ValueError:
			if ch in valid_letters:
				ans += str(to_index[ch])
	print("None" if len(ans)<=0 else ans)	

import re
s = "Rkbs,5453; Wdqiz,1245; Rwds,3890; Ujma,5589; Tbzmo,1303;"
s = re.sub(";","",s)
s = s.split(" ")
s = sorted([int(x.split(",")[1]) for x in s])
distance = []
distance.append(s[0])

for i in range(1, len(s)):
	distance.append(s[i] - s[i-1])
print(",".join(map(str,distance)))

from collections import Counter, OrderedDict
from itertools import groupby

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
        
        
import sys
from itertools import groupby
cef = open(input(),"r")	
for lines in cef:
	#series = OrderedCounter(map(int, lines.strip().split(" ")))
	ans = []
	for k, g in groupby(lines.strip().split(" ")):
		ans.append(str(len(list(g))))
		ans.append(str(k))		
	print(" ".join(ans))


s = "1232 ab+cd"	
a, b = s.split(" ")
indx = b.find("+")
if indx==-1:
	indx = b.find("-")
	ans = int(a[:indx]) - int(a[indx:])	
else:
	
	ans = int(a[:indx]) + int(a[indx:])

print(ans)

from collections import Counter
cef = open(input(), "r")
for lines in cef:
	#series = Counter(lines.strip().split(",")).most_common()
	series = lines.strip().split(" ")
	done = []
	ans = "None"
	for i in series:
		if 
	print(ans)	
	
		import sys
	
test_cases = open(input(), 'r')
for i, test in enumerate(test_cases):
    test = test.rstrip()
    if i == 0:
        j = test.index('_')
        print (test[:j] + '|' + test[j+1:])
    else:
        try:
            k = test.index('C')
        except:
            k = test.index('_')
        if k < j:
            j = k
            k = '/'
        elif k == j:
            k = '|'
        else:
            j = k
            k = '\\'
        print (test[:j] + k + test[j+1:])
test_cases.close()

cef = open(input(), "r")	
lines = cef.readlines()
for indx, line in enumerate(lines):
	if indx == 0:
		lastfind = line.find("_")
		print(line[:lastfind] + "|" + line[lastfind+1:])
	else:
		currFind  = line.find("C")	
		if currFind == -1: currFind = line.find("_")
		if currFind > lastfind:
			print(line[:currFind] + "\\" + line[currFind+1:])
			lastfind = currFind
		elif currFind < lastfind:
			print(line[:currFind] + "/" + line[currFind+1:])
			lastfind = currFind
		elif currFind == lastfind:
			print(line[:currFind] + "|" + line[currFind+1:])
		

import calendar
import sys

months = dict(zip(calendar.month_abbr[1:], range(12)))

def get_experience(ls):
    f = [[False]*12 for _ in xrange(31)]
    for p in ls:
        s, e = [i.split() for i in p.split('-')]
        i, j = months[s[0]], int(s[1])-1990
        k, l = months[e[0]], int(e[1])-1990
        while j < l or (j == l and i <= k):
            f[j][i] = True
            if i == 11:
                j += 1
                i = 0
            else:
                i += 1
    return sum(sum(r) for r in f) / 12


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print get_experience(test.split(';'))
test_cases.close()


s = "programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9"
cef = open(input(), "r")
for s in cef:
	a, b = s.split(";")
	words = a.split()
	index = [int(x) for x in b.split()]
	decoded = [""]*len(words)
	for i in range(len(index)):
		decoded[index[i] -1] = words[i]
	for i in range(len(decoded)):
		if decoded[i] == "":
			decoded[i] = words[-1]
	print(" ".join(decoded))	
		
import string
uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
lowercase, uppercase = 0, 0
cef = open(input(), "r")
for lines in cef:
	lowercase, uppercase, total = 0, 0, 0
	lines = lines.strip()
	lens  = float(len(lines))
	alllower = sum([1 for x in lines if x in lowers])
	upperpc  = ((lens - alllower) * 100) / lens
	lowerpc  = (alllower * 100) / lens	
	print("lowercase: %.2f uppercase: %.2f" %(lowerpc, upperpc))			

import sys
from string import ascii_letters
alphs = ascii_letters

cef = open(input(),"r")	

	
for line in cef:
	outs  = []
	up2lo = True
	for ch in line.strip():
		if ch in alphs:
			if up2lo==True:
				outs.append(ch.upper())				
			else:
				outs.append(ch.lower())	
			up2lo = not up2lo	
		else:
			outs.append(ch)
			
	print("".join(outs))	
				
import sys

cef = open(input(),"r")		
for deg in cef:
	deg = float(deg.strip())
	h   = int(deg)				
	m   = int((deg - h) * 60)
	s   = int((deg - h - m / 60) * 3600)
	print('{}.{:02}\'{:02}\"' .format(h, m, s))
	
alldigs=
-**----*--***--***---*---****--**--****--**---**--
*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-
*--*---*---**---**--****-***--***----*---**---***-
*--*---*--*-------*----*----*-*--*--*---*--*----*-
-**---***-****-***-----*-***---**---*----**---**--
--------------------------------------------------	


from datetime import datetime
s1 = '10:33:26'
s2 = '11:15:49' # for example
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
tdelta = '%02h%02m%02s' % (tdelta.Hour, tdelta.minute, tdelta.seconds)


import re
import sys

cef = open(input(), "r")
for lines in cef:
	lines = lines.strip()
	if len(lines) <= 55:
		print(lines)
		continue
	else:
		res = lines[:40]
		if re.match(r'\S.*', lines[40:]):
			indx = res.rfind(" ")
			if indx > -1:
				res = res[:indx]
		res = res.rstrip() + '... <Read More>'
		print(res)		

from itertools import groupby
cef = open(input(), "r")					
for lines in cef:
	lines = lines.strip()
	outs = ""	
	for k, g in groupby(lines):
		outs += k
	print(outs)	

s = {1:", yeah!",
     2:", this is crazy, I tell ya.",
     3:", can U believe this?",
     4:", eh?", 
     5:", aw yea.",
     6:", yo.",
     7:"? No way!",
     8:". Awesome!"
     }
     
tofind =[".","!","?"]     
cef = open(input(), "r")
repindex = 1
replace=False
for lines in cef:
	lines = lines.strip()		
	outs = ''
	for i,ch in enumerate(lines):
		if ch in tofind:			
			if replace:
				outs += s[repindex]				
				repindex += 1
				if repindex > 8: repindex = 1
			else:
				outs += ch	
			replace = not replace			
		else:			
			outs += ch	
	print(outs)	
		
from math import sqrt
import sys			
cef = open("codeeval.txt", "r")	
for lines in cef:
	lines = [x for x in lines.strip().split()]
	strLen = len(lines)
	matLen = int(sqrt(strLen))
	i = 0
	original = []
	while i < strLen:
		original.append(lines[i:i+matLen])
		i += matLen
	rotated = list(zip(*original[::-1])	)
	output = ""
	for i in range(matLen):
		output += " ".join(rotated[i]) +" "
	print(output)	
	'''
cef = open(input(), "r")			
for lines in cef:
	days, trans = lines.strip().split(";")
	days  = int(days)
	trans = [int(x) for x in trans.split(" ")]
	maxSum = min(trans) * len(trans)
	trades = []
	for i in range(len(trans)-days + 1):
		
		maxSum = max(maxSum, sum(trans[i:i+days]))
	print("0" if maxSum < 1 else maxSum)	
		
		
	
	

			
			
		



	



	
	
