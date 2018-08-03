def get_match_count(g, c):
    count = 0
    test  = ""
    lg = len(g)
    for i in c:
        test += i
        if len(test)>= lg:
            if test.endswith(g, -lg):
                count += 1
                test = test[:-lg]
    return count

for _ in range(int(input())):
    g = input()
    c = input()
    print(get_match_count(g, c))