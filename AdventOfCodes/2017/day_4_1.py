def is_Valid(s):
    done = []
    words= s.split()
    for word in words:
        if word in done:
            return False
    return True 
valid = 0   
with open("input.txt") as f:
    for line in f:
        valid += is_Valid(line)
print(valid)        
            
        
        