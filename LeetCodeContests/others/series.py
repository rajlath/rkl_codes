def generate_series(n):
	a = "0"
	al = [a]
	for i in range(1,n+1):
		b = al[-1]
		x = ''
		for j in b:
			x += ["01","10"][j=="0"]
		al.append(x)
	return al	
			
			

    
print(generate_series(10))           
