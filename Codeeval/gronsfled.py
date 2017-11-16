

def generateIndex(keys, val):
	pos = 0
	vlen= len(val)	
	for i, v in enumerate(keys):
		index = int(val[i % vlen])
		npos  = voc.find(v)
		deco  = voc[(npos + 84 - index) % 84]
		print i, v, index, npos, deco
			
#generateIndex('''M%muxi%dncpqftiix"''',"45162")	

voc =''' !"#$%&'()*+,-./0123456789:<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'''
with open(input(), "r") as cef:
	for lines in cef:
		key, val = lines.strip("\n").split(";")
		vlen= len(key)
		decode = ''
		for i, v in enumerate(val):
			index = int(key[i % vlen])
			npos  = voc.find(v)
			deco  = voc[(npos + 84 - index) % 84]
			decode += deco
		print(decode)	
			
		
		
		
		
		
		



