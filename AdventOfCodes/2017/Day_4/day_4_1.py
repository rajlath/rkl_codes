def is_Valid(s):
    done = []
    words= s.split()
    #print(words)
    for word in words:
        word = sorted(word)
        if word in done:
            return False
        done.append(word)
    return True 

valid = 0   
with open("input.txt") as f:    
    for line in f:
        #print(line)
        dct = set()
        words = line.strip().split()
        for k in range(len(words)):
            word = "".join(sorted(words[k]))
            print(word)
            dct.add(word)
        valid += len(dct) == len(words)
print(valid)    


        
        