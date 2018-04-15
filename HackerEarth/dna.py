d={"G":"C","C":"G","T":"A","A":"U"}
for x in input():
    if x not in d:a="Invalid Input";break
    else:a+=d[x]
print(a)
