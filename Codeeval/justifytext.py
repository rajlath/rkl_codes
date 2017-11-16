def adjustLine(candidate):
	balance = lines[len(candidate)+1:]
	balance_lst = [x for x in candidate.split(" ")]
	chcnt = sum([len(x) for x in balance_lst])
	spcneeded = 80 - chcnt
	eachspc, balspc   = divmod(spcneeded , len(balance_lst)-1)
	extra = balspc
	spc   = []
	for i in range(len(balance_lst)):
		if extra > 0:
			spc.append(eachspc + 1)
			extra -= 1
		else:
			spc.append(eachspc)
		mzip = list(zip(spc, balance_lst))		
		modifiedLine = ''.join(w + ' ' * m for m, w in mzip)
	return modifiedLine		

cef = open("justify_text.txt", "r")
for lines in cef:
	
	lines = lines.strip()	
	while(len(lines) > 80):
		lntill80 = lines[:80]
		lstspc = lntill80.rfind(" ")		
		if lntill80[-1] != " " and lines[80] != " ": 
			candidate = lntill80.rsplit(" ", 1)[0]
		else:
			candidate = lntill80		
		
		print(adjustLine(candidate))
		lines = lines[len(candidate)+1:]
	if len(lines) > 0:
		print(lines)
		
		
		
				
		
				
				
		
			
			
		
		
