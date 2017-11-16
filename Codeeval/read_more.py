cef = open("read_more.txt", "r")
for line in cef:	
	if len(line) <= 55:
		print(line)
	else:
		output = line[:40]
		indx = output.rfind(" ")	
		if indx != -1:
			output = output[:indx]
		output += "... <Read More>"	
		print(output)
	
	


