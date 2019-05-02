def conv(num,b):
    convStr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num<b:
        return convStr[num]
    else:
        return conv(num//b,b) + convStr[num%b]
nb_test = int(input())
for _ in range(nb_test):
    nums, base = [int(x) for x in input().split()]
    print(conv(nums, base))