from string import ascii_lowercase as lc
nb_test = int(input())
for _ in range(nb_test):
    nb_chr, time_repeat = [int(x) for x in input().split()]
    alpha = lc[:nb_chr]
    exclude= input()
    ans   = ""
    for i in alpha:
        if i not in exclude:
            ans += i
    print(ans * time_repeat)

