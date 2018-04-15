a = 10
b = 20
weakness = 0
if abs(a - b) == 1: print(1)
elif abs(a - b) == 2: print(2)
elif a == b:print(0)
else:
    weakness = 0
    while True:
        a+=1
        b-=1
        weakness += 2
        if a == b:
            break
        if abs(a - b) == 1:
            weakness += 2
            break
    print(weakness)

