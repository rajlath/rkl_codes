nb_test = int(input())
while nb_test > 0:
    curr = int(input())
    curr %= 6
    if curr in [0,1]:
        print("B")
    else:
        print("A")
    nb_test -= 1
