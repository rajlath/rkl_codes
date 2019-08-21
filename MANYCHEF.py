for _ in range(int(input())):
    curr = list(input())
    i = 0
    answer = ""
    while i < (len(curr)):
        if i + 4 < len(curr):
            cr = curr[i:i+4]
            if cr[0] in "C?" and cr[1] in "H?" and cr[2] in "E?" and cr[3] in "F?":
                answer += "CHEF"
                i += 4
        else:
            if curr[i] == "?":answer+="A"
            else:answer += curr[i]
            i += 1
    print(answer)        
            
        
              
        
        
        