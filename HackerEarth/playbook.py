'''
1. For the first letter return the 3rd letter counting right from it's position from the same set( i.e. if first letter is in Set 1 return letter from the same.)
2. For the second letter return the 2nd letter counting left from it's position from the next set ( i.e. if second letter is in Set 1 return letter from the Set 2.)
3. For the third letter return the 1st letter counting left from it's position from the previous set( i.e. if third letter is in Set 1 return letter from the Set 3)
4. for the fourth letter return the letter in the same position from the next set( i.e. if fourth letter is in Set 1 return letter from the Set 2)
repeat for the next letters considering the 5th as 1st and so on. If the string contains a letter more than once do not encrypt every occurence, in place of it put '.' at the end of the encrypted text.

SAMPLE INPUT 
1
legen
SAMPLE OUTPUT 
dary.
'''


sets = {
        1:"qwertyuiop",
        2:"asdfghjkl",
        3:"zxcvbnm"
        }

def get_result_set(ch, cp):
    for k, v in sets.items():
        if ch in v:
            inset = k
            pos   = v.index(ch)  
            break
    cp%=5
    if cp==0:cp=1
     
    if cp == 1:
        result_set = inset
        sl = len(sets[result_set])
        np = (pos + 3)%sl       
        return sets[result_set][np]
         
    if cp == 2:
        result_set = (inset + 1)
        if result_set == 4: result_set = 1
        sl = len(sets[result_set])
        np = pos - 2
        np  = (np + sl)%sl        
        return sets[result_set][np]
         
    if cp == 3:
        result_set = (inset -1)
        if result_set == 0: result_set=3
        sl = len(sets[result_set])
        np = pos - 1
        np = (np + sl)%sl        
        return sets[result_set][np]
         
    if cp == 4:
        result_set = (inset + 1) 
        if result_set == 4: result_set = 1
        sl = len(sets[result_set])
        np = pos%sl
        return sets[result_set][np]
             
             
     
                    
        
'''        
def get_set(ch):
    for i in range(1, 4):
        if ch in sets[i]:
            return i
            
def get_next_set(sn):
    sn += 1
    if sn == 4: sn = 1
    return sn
    
def get_previous_set(sn):
    sn -= 1
    if sn == 0: sn = 3
    return sn
                    
            
def get_result_set(setno, pos_in_word, ch):
    pos_in_word = pos_in_word % 5
    if pos_in_word == 0: pos_in_word = 1
        
    if pos_in_word == 1:        
        return sets[setno][2]
        
    if pos_in_word == 2:        
        ipos = sets[setno].index(ch)        
        lens = len(sets[setno])
        setno = get_next_set(setno)
        return sets[setno][(ipos - 2 + lens) % lens]
        
    if pos_in_word == 3:             
        ipos = sets[setno].index(ch)
        lens = len(sets[setno])
        setno = get_previous_set(setno)        
        return sets[setno][(ipos - 1 + lens) % lens]
         
    if pos_in_word == 4:           
        ipos  =  sets[setno].index(ch)
        lens = len(sets[setno])        
        setno =  get_next_set(setno)        
        return sets[setno][(ipos+lens) % lens]
        
'''        
        
for _ in range(int(input())):
    s = raw_input() 
    s1 = ""
    repeats = []
    for a in s:
        if a in repeats:
            continue
        else:
            repeats.append(a)
            s1 += a 
    ans = ""
    repeated = len(s) - len(s1)
    for i,v  in enumerate(s1):        
        a = get_result_set(v, i+1)        
        ans = ans + a
    print(ans + ("." * repeated))      
         




    
         
               
            
'''
if first return set[2] from same set
if second return next set set[1]
if third  return previous set one pos less then found
if fourth return nextset same position
'''
