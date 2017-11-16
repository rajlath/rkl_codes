'''
$#**\0100000101101100011100101000

'''

import sys
import re




cef = open(sys.argv[1], "r")
for lines in  cef:
    lines = lines.strip()
    msg   = re.split(r"[01]+", lines)


	
    keys  = msg[0]
	
    coded = lines[len(keys):]	
	
    allkeys = []
    cnt   = 0
    tmp   = coded

    while True:		
	    binlen = int(tmp[:3], 2)
	    #print("binlen:", binlen)
	    if tmp[:3] == "000": break		
	    tmp = tmp[3:]
	    #print(tmp)
	    i = 0
	    while i < len(tmp):
            nextkey = tmp[:binlen]
            if nextkey == "1" * binlen:                
			    tmp = tmp[binlen:]
			    #print("After",tmp)
			    break
		    else:
		        tmp = tmp[binlen:]
			    allkeys.append(nextkey)
			    i += binlen	
	    if len(tmp) <= 0:
		    break
    index = 0
    mapping = {}
    for c in list(keys):
	    key = get_key_for_index(index)
	    mapping[key] = c
	    index += 1
    decoded = ""
    for a in allkeys:
        decoded += mapping.get(a, "")
    print(decoded)	    		
		
			
		
				
				
			
			
		
		
		
