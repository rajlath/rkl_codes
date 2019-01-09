R=lambda:[int(x) for x in input().split()]
nb_cases = int(input())
for _ in range(nb_cases):
    ins = input()
    if len(ins) <= 10:
        print(ins)
    else:
        print(ins[0] + str(len(ins) - 2) + ins[-1])



