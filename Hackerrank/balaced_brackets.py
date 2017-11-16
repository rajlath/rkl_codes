'''
Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}
Sample Output

YES
NO
YES
'''
opens = ["(", "[", "{"]
clos= [")", "]", "}"]
brackets = {")":"(", "]":"[", "}":"{"}
for i in range(int(input())):    
    br  = []
    ans = "YES"
    s = input()
    for x in s:        
        if x in opens:
            br.append(x)
        else:
            if not br:
                ans = "NO"
                break
            y = br.pop()
            if y != brackets[x]:
                ans = "NO"
                break
    if len(br)>0:ans = "NO"        
    print(ans)        
            
                  
            
      