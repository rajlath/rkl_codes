lens = int(input())
score= [x for x in input().split()]
ans  = "EASY"
for i in score:
    if i is "1":
        ans = "HARD"
        break
print(ans)