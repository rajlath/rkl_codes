import sys

cef = open("brainfck.txt", "r")
for line in cef:
    p = 0
    bstack = []
    b = {}
    f = False
    
    for i, s in enumerate(line):
        if s == "[":
            bstack.append(i)
        elif s == "]":
            if len(bstack)==0:
                f = True
                break
            b[bstack[len(bstack)-1]], b[i] = i, bstack[len(bstack)-1]
            bstack = bstack[:len(bstack)-1] 
    if f and len(bstack) > 0:
        print("Invalid expression containing unmatched brackets.")  
        continue
        
       
        
    t = [0]
    i = 0
    output = ""
    while i < len(line):
             
        curr = line[i]        
        if curr == "+":
            t[p] += 1            
            if t[p] == 256: t[p] = 0
        elif curr == "-":
            t[p] -= 1
            if t[p] == -1: t[p] = 255
        elif  curr == ".":            
            output += chr(t[p])
        elif  curr == ",": t[p] = int(input())      
        elif  curr == "<":
            if p > 0: p-=1
            else: t = [0]+t
        elif  curr == ">":
            p += 1
            if p == len(t): t.append(0) 
        elif  curr == "[":            
            if t[p] == 0:                    
                i = b[i]
        elif  curr == "]":
            if t[p] != 0:
                i = b[i]
        i+=1        
    print(output)            
          
                        
                        
                
    
