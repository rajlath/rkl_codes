s = "301212"
start = 0
end   = 0
s = list(s)
for i in range(len(s)):	
	s[start]^=s[end]
	s[end]^=s[start]
	s[start]^= s[end]
	start+=1
	end += 1
print("".join(s))	
	
	
