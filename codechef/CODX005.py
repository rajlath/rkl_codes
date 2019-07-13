lens = int(input())
strs = input()
curr = strs[0]
done = False
strs = strs[1:]
for cur in strs:
    if not done and cur != curr:
        done = True
        lens -= 1
    else:
        done = False
    curr = cur    
print(lens)
