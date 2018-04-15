import copy
def pairing(l):
    def rec(l, choice):
        if l == []:
            print (choice)
        else:
            for j in range(1, len(l)):
                choice1 = choice + [(l[0],l[j])]
                l1 = copy(l)
                del l1[j]
                del l1[0]
                rec(l1, choice1)
    rec(l, [])

print(pairing(range(1, 10)))
