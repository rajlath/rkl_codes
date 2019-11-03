distance, alex, ryan = [int(x) for x in input().split()]
atime = distance // alex
rtime = distance // ryan
if atime == rtime:
    print("Draw")
elif atime > rtime:
    print("Ryan")
else:
    print("Alex")
