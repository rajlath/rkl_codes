nb_test = int(input())
ans =[]
for i in range(nb_test):
    ans += [input()]
    ans = sorted(ans)
print("".join(ans))

