a, b = [x for x in input().split()]
abin = bin(int(a))[2:]
bbin = bin(int(b))[2:]
#print(abin, bbin)

if abin.count("1") == bbin.count("1") and abin.count("0") == bbin.count("0"):
    print("good")
else:
    print("bad")