ins = "raj kumar lath bargarh      odissa"
ans = ''
for i in ins:
    if i.isspace():
        ans = " "+ans
    else:
        ans += i
print(ans)
