'''
2
5 3 2
1 2 3 4 5
5 2 4
1 2 3 4 5
'''
nb_test = int(input())
for _ in range(nb_test):
    n, a, b = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    while arr:
        l = len(arr)
        arrr = [x for x in arr if x % a != 0]
        if len(arrr) == l:
            print("ALICE")
            break
        else:
            l = len(arrr)
            arrr = [x for x in arrr if x % b != 0]
            if l == len(arrr):
                print("BOB")
                break
        arr = arrr[:]


