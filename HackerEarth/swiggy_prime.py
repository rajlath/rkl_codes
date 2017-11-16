n = input()
ans = ""
for i in range(len(n)-1, 0, -1):
    curr = n[i]
    if curr == 1 and i == 0:
        break
    if curr == "2":
        ans += curr
    elif curr == "3":
        ans += "2" 
    elif curr in ["4", "5"]:
        ans += "3"
    elif curr in ["6", "7"]:
        ans += "5"
    else:
        ans +="7" 
    print(ans)    
print("".join(ans[::-1]))           
                       
        
        
            
    
