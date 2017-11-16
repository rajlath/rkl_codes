'''
5
5 4 1 3 2
'''
def is_empty(s):
    return len(s)==0
def top(s):
    if len(s)> 0:
        return s[-1]
    else:
        return  False
                
st = []
noe = int(input())
front = [None] * noe
back  = [None] * noe
arr = [int(x) for x in input().split()]
for i,v in enumerate(arr, 1):
    if is_empty(st) or arr[top(st)] >= arr[i]:
        st.append(i)
    else:
        while not is_empty(st) and arr[top(st)] < arr[i]:
            front[top(st)] = i
            st.pop()
            st.append(i)
    
while not is_empty(st):
    front[top(st)] = -1
    st.pop()
    
for i in range(noe-1, -1, -1):
    if is_empty(st) or arr[top(st)] >- arr[i]:
        st.append(i)
    else:
        while not is_empty(st) and arr[top(st)] < arr[i]:
            back[top(st)] = i
            st.pop()
            st.append(i)
while not is_empty(st):
    back[top(st)] = -1
    st.pop()    

print(front, back)    
for i in range(noe):
    print(front[i] + back[i],end=" ")                    
    
    
          
            
            
            



