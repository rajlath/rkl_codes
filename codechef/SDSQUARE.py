import math
power_list = []
for i in range(1, 100001):
    curr = i * i
    is_valid = True
    while curr:
        if curr % 10 in [0,1,4,9]:
            curr//=10
        else:
            is_valid = False
            break
    if is_valid:power_list.append(i)
print(power_list)    
