import re
import sys

cef = open("sys.argv[1]", "r")
for lines in cef:
	a, b, x, y = map(int,re.findall("(\d+)", lines.strip()))
	r = 0
	while b != y:
		r, a, b, x, y = r+a, b-1, a, b-y, x
	print( r + x)

