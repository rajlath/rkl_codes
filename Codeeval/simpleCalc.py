
precedence = {"^":3, "*":2, "/":2, "+":1, "-":1}

def calculate(a, b, c):
	if b == "^":
		return a ** b
	elif b == "*":
		return a * b
	elif b == "/":
		return a / b
	elif b == "+":
		print(a, b, c)
		return a + b
	elif b == "-":
		return a - b
	else:
		pass
		
import re

def parse(exp):
	rpn = []
	state = 0
	while len(exp) > 0:
		if state == 0:
			if exp[0] == "(":
				rpn.append("(")
				exp = exp[1:]				
			else:
				r = re.compile("(^[-]?[0-9]+([.][0-9]+)?)")
				matches = r.search(exp).groups()
				print(matches)
				if exp[0] == '-'  and  exp[1] == '(':
					rpn.append('[')
					exp = exp[2:]
				else:
					rpn.append(float(matches[0]))
					exp = exp[len(matches[0]):]
					state = 1
		else:			
			if  exp[0] in '^*/+-':
				rpn.append(exp[0])
				exp = exp[1:]
				state = 0
				
				if len(exp) > 3 and exp[-2] != ')' and  rpn[-3] != '(' and  rpn[-3] != '[' and rpn[-4] != ')':
					if precedence[rpn[-3]] >= precedence[rpn[-1]]:
						rpn[-4] = calculate(float(rpn[-4]), rpn[-3], float(rpn[-2]))
						rpn = rpn[:-4].append(rpn[-1])
						
			elif exp[0] == ')':
				rpn.append(")")
				exp = exp[1:-1]
				while len(rpn) > 3 and rpn[-2] != ')' and  rpn[-3] != '(' and  rpn[-3] != '[' and rpn[-4] != ')':
					rpn[-4] = str(calculate(float(rpn[-4]), rpn[-3], float(rpn[-2])))
					rpn = rpn[:-4] .append(rpn[-1])
				if rpn(len) > 3 and  rpn[-3] == '(':
					rpn = rpn[:-3].append(rpn[-2])
				elif len(rpn) > 3 and  rpn[-3] == '[':
					rpn  = rpn[:-3].append(-rpn[-2])
				elif len(rpn) == 3 and  rpn[0] == '(':
					rpn = [rpn[1]]
				elif len(rpn) == 3 and  rpn[0] == '[':
					rpn = [-rpn[1]]
					
			print(rpn)	
	return rpn
	
print(parse("(((5+2)-((3))*1)-1)-1"))				   
				   
				   
       
				
        
					
		
						
			
