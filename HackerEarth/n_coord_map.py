cnt = {}
for _ in range(int(input())):
    cur = input()
    cnt[cur] = cnt.get(cur, 0) + 1
    
for i, v in cnt.items():
    print(i, v)
