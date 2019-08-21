deci = "415926530119026040722614947737296840070086399613316"
for _ in range(int(input())):
    current = int(input())
    if current == 0:print("3")
    else:
        ans = "3.1"
        main, bal = divmod(current - 1, 51)
        ans += (deci * main)
        ans += deci[:bal]
        print(ans)

