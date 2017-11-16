#for i in range(1,101):print("Fizz"*(i%3<1)+"Buzz"*(i%5<1) or i) #  python3 63


#i=0;exec"print i%3/2*'Fizz'+i%5/4*'Buzz'or-~i;i+=1;"*100 # python2 54

#codeeval
'''
first = 3
second=5
limit = 20
'''

'''	
	lst = []
	first, second, limit = [int(x) for x in line.strip().split(" ")]
	
	for i in range(1,limit+1):
		curr = ("F" * (i%first<1) + "B" * (i%second<1) or i)
		lst.append(curr)
	print (" ".join(map(str, lst))	)

print(" ".join("hello worlds".split(" ")[::-1]))

x = 13 ; n = 8
i=2
while True:
	if n * i >= x:
		print(n * i)
		break
	i+=1


cef = open("codeeval.txt", "r")
lines = cef.readlines()	
for line in lines:
	a, p1, p2 = map(int, line.strip().split(","))
	res = "true"
	bins = bin(a)[2:][::-1].rjust(8,"0")
	print(bins)
	if bins[p1-1] != bins[p2-1]:
		print("false")
	else:
		print("true")	
		

print("This is some text"	.lower())

print(sum([int(x) for x in "696"]))
'''
def getFibo(n):
	if n <=1:
		return 1
	else:
		return getFibo(n-1) + getFibo(n - 2)	

print(getFibo(11))		



		
		
		
		
		
	
	


