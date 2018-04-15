for i in range(2,101):
    non=0
    for x in range(2,101):
        if i%x==0:
            non=1;break
    if non==0:print(i)
