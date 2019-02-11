def find_next_partition(n):
    ns = str(n)
    for i in range(len(ns)-1):
        one = ns[:i+1]
        two = ns[i+1:]
        print(one, two, "first")
        if int(one) < int(two) and one != two:
                return (one, two)


nb_test = int(input())
for  _ in range(nb_test):
    lens = int(input())
    n    = int(input())
    ns   = str(n)
    ans  = "NO"
    for i in range(len(ns) - 1):
        one = ns[:i+1]
        two = ns[i+1:]
        if int(one) < int(two) and one != two:
            ans = "YES"
            break
    print(ans)
    if ans == "YES":
        print("2")
        print(one, two)


