index = {0:"h", 1:"a",2:"c",3:"k",4:"e",5:"r",6:"r",7:"a",8:"n",9:"k"}
for _ in range(int(input())):
    ins = input()
    i = 0
    c = 0
    for x in ins:

        if x == index[i]:i+=1
        if i == 10:break
    if i == 10:
        print("YES")
    else:
        print("NO")