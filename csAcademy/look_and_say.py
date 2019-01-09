# Parameter n is an integer
# The function should return a string
import re

repeating_digits = re.compile(r'((\d)\2*)')

def look_and_say(n):
    ans = "1"
    i = 1
    while n > i:
        ans = helper(ans)
        i += 1
    return ans    
        

def helper(n):
    curr = ''
    for match, char in repeating_digits.findall(n):
        curr += str(len(match))        
        curr += char        
    return curr
        
    
    
    
    
###
n = int(input())
answer = look_and_say(n)
print(answer)


    
  
    
    
    
