nb_test = int(input())
for _ in range(nb_test):
    a,b = [int(x) for x in input().split()]
    fail= "cannot distribute"
    if b == 0:
        print(fail)
    else:
        divs = a // b
        print([fail, divs][divs > 0])

