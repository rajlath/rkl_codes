'''
S.push(st[0]);
  //cout<<S.topEl();//<<endl;
  int p=1;
 // cout<<st[p]<<endl;
  while(p!=len){
   if(S.topEl()==st[p]) S.pop();
   else
   S.push(st[p]);
  // cout<<endl<<endl<<S.topEl()<<endl;
   p++;
  } 
  if (S.isEmpty()) result ++; 
 } cout<<result;
 
 3
ABAB
AABB
ABBA

3
AAA
AA
AB
'''
for _ in range(int(input())):
    stack = []
    result= 0
    st = input()
    stack.append(st[0])
    for i in range(1, len(st)):
        if stack[-1] == st[i]:
            stack.pop()
        stack.append(st[i])                
    if len(stack)==0:result += 1
    
if len(stack)==0:result += 1    
print(result)            
                   
        
            
