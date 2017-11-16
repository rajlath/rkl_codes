

import sys
import re

def int_to_binary_string(x, length=0):
    formatter = "{:0" + str(length) + "b}"
    return formatter.format(x)

def zero_string_of_length(length):
    result = ""
    for i in range(length):
        result += "0"
    return result

def is_all_ones(s):
    for c in s:
        if c != '1':
            return False
    return True

key_cache = {}
def get_key_for_index(index):
    if index in key_cache:
        return key_cache[index]
    if index == 0:
        result = zero_string_of_length(1)
    else:
        previous = get_key_for_index(index-1)
        previous_plus_one = int_to_binary_string(int(previous, 2) + 1,
                                                 len(previous))
        if is_all_ones(previous_plus_one):
            result = zero_string_of_length(len(previous) + 1)
        else:
            result = previous_plus_one
    key_cache[index] = result
    return result


cef = open(input(), "r")
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
		
			
		
				
				
			
			
		
		
		
