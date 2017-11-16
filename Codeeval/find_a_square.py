import sys
import re
import math

def distance(c1, c2):
    return math.sqrt( abs(c1[0]-c2[0])**2 + abs(c1[1]-c2[1])**2 )

def is_square(points):
	allDistance = {}
	for i, c in enumerate(points):
		rest = points[:i] + points[i+1:]
		for r in rest:
			dist = distance(c, r)
			allDistance[dist] = allDistance.get(dist, 1) + 1
	return len(allDistance) == 2

	
	
with open(input(), "r") as cef:
	reg = re.compile('\((\d+)?,(\d+)\)')
	lines = cef.readlines()
	for line in lines:
		points = reg.findall(line)
		points = sorted((int(j[0]), int(j[1])) for j in points)
		print( 'true' if is_square(points) else 'false')
		
                    
