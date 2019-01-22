matches = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
nb_test = int(input())
for _ in range(nb_test):
    ins = sum([matches[int(x)] for x in input()])
    ans = ""
    if ins%2==1 and ins >= 3:
        ans = "7"
        ins -= 3
    #print(ins)
    ans += (ins//2) * "1"
    print(ans)