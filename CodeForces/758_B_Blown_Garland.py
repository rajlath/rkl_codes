s=input()
d={}
ct=[0,0,0,0]
for i,c in enumerate(s):
	if c=='!':
		ct[i%4]+=1
	else :
		d[c]=i%4
for i in "RBYG":
	print(ct[d[i]])
    