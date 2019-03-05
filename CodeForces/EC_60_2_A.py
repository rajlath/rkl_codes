'''
6 9 2
1 3 3 7 4 2
54
'''
noe, will_do, can_do = [int(x) for x in input().split()]
satisfy = sorted([int(x) for x in input().split()], reverse=True)
a, b = satisfy[0], satisfy[1]
if can_do >= will_do or a == b:
    print(a * will_do)
else: 
    times = will_do // (can_do + 1)
    ans = a * times * can_do + b * times    
    rest = will_do % (can_do + 1)
    ans += rest * a
    print(ans)



      
