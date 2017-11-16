from string import ascii_uppercase as uc, ascii_lowercase as lc
arr = [i for i in range(256)]
table = {chr(k): k for k in range(256)}



for _ in range(int(input())):
    x, y = input().strip().split()
    a, b = table[x], table[y]
    arr[a], arr[b] = arr[b], arr[a]
    table[x], table[y] = b, a
 
    map = {}
    for idx, v in enumerate(arr):
        map[chr(idx)] = chr(v)
    
    s = input()
    ans = []
    for c in s:
        if c.islower():
            ans.append(map[c.upper()].lower())
        else:
            ans.append(map[c])
 
        print(''.join(ans))
