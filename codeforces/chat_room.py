s = input()
word = "hello"
lastIndx = -1
notOk = False
for i,v in enumerate("hello"):
    
    if s.index(v) > lastIndx:
        lastIndx = i
    else:
        notOk = True
        break
print("NO" if notOk else "YES")        
            


