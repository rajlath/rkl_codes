import sys

def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(22000):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2
            
piDigits = []
for i in make_pi(): 
	piDigits.append(str(i))
	
	

with open(input(), "r")	as cef:
	lines = cef.readlines()
	for line in lines:
		if len(line) <= 0: continue
		print(piDigits[int(line) -1])
		
	
		
	
