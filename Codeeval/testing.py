s = "Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn't look."

spaces = [i for i, ltr in enumerate(s) if ltr == " " and i <=40]
lastIndex = spaces[-1]
if lastIndex == 40:
	lastIndex = spaces[-2]
print(s[:lastIndex]+"... <Read More>")	
