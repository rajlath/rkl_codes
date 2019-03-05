mods = 1000000007
ans = [0] * 1000001

def seive():
    global ans
    v = [0] * 1000001
    for i in range(1000001):ans[i] = i
    ans[1] = 1
    for i in range(2, 1000001):
        if v[i] == 0:
            for j in range(i, 1000001, i):
                v[j] = 1
                ans[j] = ans[j]//i
                ans[j] = ans[j] * (i - 1)
    ans = [(ans[i] + ans[i-1])%mods for i  in range(1, 1000001)]

seive()
nb_test = int(input())
for _ in range(nb_test):
    n = int(input())
    print( (ans[n] * ans[n]) % mods )


