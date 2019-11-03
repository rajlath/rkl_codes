for _ in range(int(input())):
    n, q = [int(x) for x in input().split()]
    ins = input()
    for _ in range(q):
        a, l, r = [int(x) for x in input().split()]
        if a == 1:
            print(["O", "E"][sum([1 for x in ins[l-1:r] if x=="O"])%2==0])
        else:
            print(["O", "E"]["E" in ins[l-1:r]])