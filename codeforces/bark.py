password = input()
v_count  = int(input())
could_be = ""
for i in range(v_count):
    could_be += input()
        
print("YES" if password in  set(could_be) else "NO")        
           
