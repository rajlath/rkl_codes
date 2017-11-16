'''
7 6
4 3 7 6 7 2 2
'''
noe, can_do = [int(x) for x in input().split()]
marks = [int(x) for x in input().split()]
skipped = False
cnt = 0
for i in marks:
    if i <= can_do: cnt += 1
    elif not skipped:
        skipped = True
        continue
    else:
        break
print(cnt)            


