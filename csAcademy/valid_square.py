#!/usr/bin/env python
# -*- coding: utf-8 -*-# 
# 23.08.2018 20:23:23 
# oorja
# copyright 2018   oh!   oorja.halt@gmail.com
from math import sqrt
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
def distance(a, b):
	return int(sqrt(pow(a.x - b.x, 2) + (pow(a.y - b.y, 2))))	
		
points = []
for _ in range(int(input())):
	for _ in range(4):
		a, b = [int(x) for x in input().split()]
		points.append(Point(a, b))		
	side1 = distance(points[0], points[1])
	side2 = distance(points[1], points[2])
	side3 = distance(points[2], points[3])
	side4 = distance(points[3], points[0])
	diag1 = distance(points[0], points[2])
	diag2 = distance(points[1], points[3])
	print(side1, side2, side3, side4, diag1, diag2)
	print(side1==side2==side3==side4 and diag1 == diag2)
	
	
	
