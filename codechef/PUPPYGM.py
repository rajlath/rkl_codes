for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    print(["Vanka","Tuzik"][a%2==0 or b%2==0])
    