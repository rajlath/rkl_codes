def survivor(n):
	'''
	to find out survivor in a circular arrangement
	gap = nth person to get killed
	param n int : nos of person
	return  : n int no of person survived
	'''
	first = 1
	gap   = 2 # assuming every person kills their neighbours
	
	while n > 1:
		if n%2 : first += gap*2
		else:gap *= 2
		n//= 2
	return first
	
print(survivor(10))		
