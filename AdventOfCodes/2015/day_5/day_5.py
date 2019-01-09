import re
repeat_re = re.compile(r"(.).\1")
dup_pair_re = re.compile(r"(..).*\1")
vowel_re = re.compile(r"[aeiou]")
dup_re = re.compile(r"(.)\1")
exclude_re = re.compile(r"(ab|cd|pq|xy)")

def check_if_valid(st):
    stack = ["-"]    
    vowels=0 
    has_double = False
    invalid = ['ab', 'cd', 'pq', 'xy']    
    for i in st:
        curr = stack[-1] + i
        if curr in invalid:
            return False        
        if i in "aeiou":vowels += 1        
        if i == stack[-1]:has_double = True
        stack.append(i)
        
    return vowels >= 3 and has_double

def is_nice(word):
    if exclude_re.search(word):
        return False
    vowel_count = len(vowel_re.findall(word))
    dup = dup_re.search(word)
    return (vowel_count >= 3 and dup is not None)

def check_if_valid_2(st):
    '''
    hastwin = False
    hastrip = False
    stack = []
    for i in range(0, len(st)-1, 1):
        curr = st[i:i+2]        
        if curr in stack:
            hastwin= True
            break
        stack.append(curr)
        
    for i in range(0, len(st)-2,1):
        curr = st[i:i+3]        
        if curr[0] == curr[-1]:
            hastrip = True            
            break
    return  hastwin==True and hastrip == True  
    '''
    if repeat_re.search(st) is None:
        return False
    return dup_pair_re.search(st) is not None
        
        
        
        


print(check_if_valid_2("uurcxstgmygtbstg"))

lines = open("input.txt").readlines()
nice = 0
for line in lines:
    nice += check_if_valid_2(line.strip())
print(nice) 
 

    