nb_test = int(input())
for _ in range(nb_test):
    log = input()
    ans = "yes"
    for i in range(0, len(log), 2):
        curr = log[i:i+2]
        print(curr)
        if curr is "AA" or curr == "BB":
            ans = "no"
            break
    print(ans)

