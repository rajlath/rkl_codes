s = input()
cnt = len(s.replace("144",'').replace("14",'').replace("1", ''))
if cnt > 0:
    print("NO")
else:
    print("YES")