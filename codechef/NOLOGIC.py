from string import ascii_lowercase as lc
for _ in range(int(input())):
    current = [x.lower() for x in input() if x in lc]
    current = set(current)    
    if len(current)== 26:
        print("~")
    elif len(current) == 0:
        print("a")
    else:
        for i in lc:
            if i not in current:
                print(i)
                break