ans,a = '',"GCTA"
for x in input():
    if x not in a:
        ans = "Invalid Input";break
    else:ans+= "CGAU"[a.find(x)]
print(ans)


