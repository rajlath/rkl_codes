no_team, no_problem = [int(x) for x in input().split()]
is_ok = True
for i in range(no_team):
    arr = [int(x) for x in input().split()]
    if sum([x for x in arr]) < no_problem //2:is_ok = False
print("YES" if is_ok else "NO")    
        
