import re

begin = "1113122113"
#begin  = "1233"
repeating_digits = re.compile(r'((\d)\2*)')
#print(repeating_digits.findall(begin))

for _ in range(50):
    curr = ''
    for match, char in repeating_digits.findall(begin):        
        curr += str(len(match))        
        curr += char        
    begin = curr
    #print(begin)
print(len(begin))    

        
    

        
        

