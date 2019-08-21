from collections import defaultdict

def update_counts(word,  mode):
    global cnt
    for i in word:
        if i not in cnt:
            cnt[i]= [0, 0]
        cnt[i][mode] += 1

for _ in range(int(input())):
    a = input()
    b = input()
    cnt = defaultdict(list)
    update_counts(a, 0)
    update_counts(b, 1)
    commons = 0
    for i in cnt:
        commons += min(cnt[i])
    print(commons)